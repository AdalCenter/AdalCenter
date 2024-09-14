from django.db import models
import qrcode
from django.core.files import File
from io import BytesIO
from django.conf import settings


class Observer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    contact_number = models.CharField(max_length=50, verbose_name="Контактный номер")
    address = models.TextField(verbose_name="Адрес")
    certificate_duration = models.CharField(max_length=50, verbose_name="Срок сертификата")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наблюдатели'
        verbose_name_plural = 'Наблюдатель'

class Service(models.Model):
    photo = models.ImageField(upload_to='service-images/', verbose_name='Фото какого-то сервиса')
    service = models.CharField(max_length=64, unique=True, verbose_name="Тип обслуживания")

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Сервисы'
        verbose_name_plural = 'Сервис'

class CertifiedCompany(models.Model):
    company_email = models.EmailField()
    certificate_name = models.CharField(max_length=28)
    company_photo = models.ImageField(upload_to='company_photos/', verbose_name="Фото компании (внутри или снаружи)")
    company_name = models.CharField(max_length=255, verbose_name="Название компании")
    trademark = models.CharField(max_length=255, verbose_name="Товарный знак")
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Тип обслуживания", related_name="companies")
    registration_number = models.CharField(max_length=100, verbose_name="Регистрационный номер")
    region = models.CharField(max_length=255, verbose_name="Область")
    observer = models.ForeignKey(Observer, on_delete=models.SET_NULL, null=True, verbose_name="Наблюдатель")
    company_address = models.TextField(verbose_name="Адрес компании")
    certificate_photo = models.ImageField(upload_to='certificate_photos/', verbose_name="Фото сертификата")
    qr_code = models.ImageField(upload_to='qr_codes/', verbose_name="QR-код", blank=True, null=True)
    issue_date = models.DateField(auto_created=True, verbose_name="День получения")
    expiration_date = models.DateField(auto_created=True, verbose_name="Дата окончания")
    CERTIFICATE_TYPE_CHOICES = [
        ('Сертифицированный', 'Сертифицированный'),
        ('В процессе', 'В процессе'),
        ('Приостоновлено', 'Приостоновлено'),
        ('Истекшие', 'Истекшие')
    ]
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_TYPE_CHOICES, default='В процессе', verbose_name="Тип сертификата")

    def save(self, *args, **kwargs):
        if not self.qr_code and self.certificate_photo:
            download_url = f'https://{settings.SITE_DOMEN}.com{self.certificate_photo.url}'

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(download_url)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            self.qr_code.save(f'qr_{self.pk}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Сертифицированные компании'
        verbose_name_plural = 'Сертифицированная компания'
