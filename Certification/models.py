from django.db import models
import qrcode
from django.core.files import File
from io import BytesIO
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


class Observer(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Ф.И.О")
    observer_profile_image = models.ImageField(upload_to='ObserverProfileImage/', verbose_name='Фото профиля наблюдателя')
    contact_number = models.CharField(max_length=50, verbose_name="Контактный номер")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return f'{self.fullname} - {self.contact_number}'

    class Meta:
        verbose_name = 'Наблюдатель'
        verbose_name_plural = 'Наблюдатели'

class Service(models.Model):
    photo = models.ImageField(upload_to='service-images/', verbose_name='Фото какого-то сервиса')
    service = models.CharField(max_length=64, unique=True, verbose_name="Тип обслуживания")

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

class CertifiedCompany(models.Model):
    company_email = models.EmailField(verbose_name='Электронная почта компании')
    certificate_name = models.CharField(max_length=28, verbose_name='Название сертификата')
    company_photo = models.ImageField(upload_to='company_photos/', verbose_name="Фото компании (внутри или снаружи)")
    company_name = models.CharField(unique=True, max_length=255, verbose_name="Название компании")
    trademark = models.CharField(unique=True, max_length=255, verbose_name="Товарный знак")
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Тип обслуживания", related_name="companies")
    registration_number = models.CharField(unique=True, max_length=100, verbose_name="Регистрационный номер")
    region = models.CharField(max_length=255, verbose_name="Область")
    observer = models.ForeignKey(Observer, on_delete=models.SET_NULL, null=True, verbose_name="Наблюдатель")
    company_address = models.TextField(unique=True, verbose_name="Адрес компании")
    certificate_photo = models.ImageField(upload_to='certificate_photos/', verbose_name="Фото сертификата")
    qr_code = models.ImageField(upload_to='qr_codes/', verbose_name="QR-код", blank=True, null=True)
    issue_date = models.DateTimeField(verbose_name="Дата и времени получения сертификата", blank=True, null=True)
    expiration_date = models.DateTimeField(verbose_name="Дата и времени окончания сертификата", blank=True, null=True)
    certificate_type = models.CharField(max_length=50, choices=[('Сертифицированный', 'Сертифицированный'), ('В процессе', 'В процессе'), ('Приостановлено', 'Приостановлено'), ('Истекший', 'Истекший')], default='В процессе', verbose_name="Тип сертификата")

    def __str__(self):
        return self.company_name

    def update_certificate_type(self):
        now = timezone.now()
        if self.certificate_type != 'Приостановлено':
            if self.expiration_date and self.expiration_date < now:
                self.certificate_type = 'Истекший'
            else:
                self.certificate_type = 'Сертифицированный'

    def clean(self):
        if self.certificate_type == 'В процессе':
            if self.issue_date or self.expiration_date:
                raise ValidationError("Нельзя указывать даты получения и окончания сертификата, если тип сертификата 'В процессе'.")

        if self.certificate_type != 'В процессе':
            if not self.issue_date or not self.expiration_date:
                raise ValidationError("Для этого типа сертификата необходимо указать даты получения и окончания.")

        if self.pk:
            original = CertifiedCompany.objects.get(pk=self.pk)
            if original.certificate_type == 'Приостановлено' and self.certificate_type != 'Приостановлено':
                raise ValidationError("Нельзя изменить тип сертификата с 'Приостановлено' на другой.")

    def save(self, *args, **kwargs):
        self.update_certificate_type()
        self.full_clean()
        super().save(*args, **kwargs)

    def get_certificate_status_icon(self):
        if self.certificate_type == 'Сертифицированный':
            return './CertificateStatusIcon/Verified.png'
        elif self.certificate_type == 'В процессе':
            return './CertificateStatusIcon/In_progress.png'
        elif self.certificate_type == 'Приостановлено':
            return './CertificateStatusIcon/Suspended.png'
        elif self.certificate_type == 'Истекший':
            return './CertificateStatusIcon/Expired.png'

    def get_certificate_status_text(self):
        if self.certificate_type == 'Сертифицированный':
            return 'Проверенный Сертифицировано до'
        elif self.certificate_type == 'В процессе':
            return 'В процессе'
        elif self.certificate_type == 'Приостановлено':
            return 'Приостановлено'
        elif self.certificate_type == 'Истекший':
            return 'Истекший'

    class Meta:
        verbose_name = 'Сертифицированная компания'
        verbose_name_plural = 'Сертифицированные компании'
