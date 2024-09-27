from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings


class Observer(models.Model):
    fullname = models.CharField(max_length=255, verbose_name=_("Ф.И.О"))
    observer_profile_image = models.ImageField(upload_to='ObserverProfileImage/', verbose_name=_('Фото профиля наблюдателя'))
    contact_number = models.CharField(max_length=50, verbose_name=_("Контактный номер"))
    address = models.TextField(verbose_name=_("Адрес"))

    def __str__(self):
        return f'{self.fullname} - {self.contact_number}'

    class Meta:
        verbose_name = _('Наблюдатель')
        verbose_name_plural = _('Наблюдатели')


class Service(models.Model):
    photo = models.ImageField(upload_to='service-images/', verbose_name=_('Фото какого-то сервиса'))
    service = models.CharField(max_length=64, unique=True, verbose_name=_("Тип обслуживания"))

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = _('Сервис')
        verbose_name_plural = _('Сервисы')


class CertifiedCompany(models.Model):
    company_email = models.EmailField(verbose_name=_('Электронная почта компании'))
    certificate_name = models.CharField(max_length=28, verbose_name=_('Название сертификата'))
    company_photo = models.ImageField(upload_to='company_photos/', verbose_name=_("Фото компании (внутри или снаружи)"))
    company_name = models.CharField(unique=True, max_length=255, verbose_name=_("Название компании"))
    trademark = models.CharField(unique=True, max_length=255, verbose_name=_("Товарный знак"))
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_("Тип обслуживания"), related_name="companies")
    registration_number = models.CharField(unique=True, max_length=100, verbose_name=_("Регистрационный номер"))
    region = models.CharField(max_length=255, verbose_name=_("Область"))
    observer = models.ForeignKey(Observer, on_delete=models.SET_NULL, null=True, verbose_name=_("Наблюдатель"))
    company_address = models.TextField(unique=True, verbose_name=_("Адрес компании"))
    certificate_photo = models.ImageField(upload_to='certificate_photos/', verbose_name=_("Фото сертификата"))
    qr_code = models.ImageField(upload_to='qr_codes/', verbose_name=_("QR-код"), blank=True, null=True)
    issue_date = models.DateTimeField(verbose_name=_("Дата и времени получения сертификата"), blank=True, null=True)
    expiration_date = models.DateTimeField(verbose_name=_("Дата и времени окончания сертификата"), blank=True, null=True)

    # Перевод choices
    CERTIFICATE_CHOICES = [
        ('Сертифицированный', _('Сертифицированный')),
        ('В процессе', _('В процессе')),
        ('Приостановлено', _('Приостановлено')),
        ('Истекший', _('Истекший')),
    ]
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_CHOICES, default='В процессе', verbose_name=_("Тип сертификата"))

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
                raise ValidationError(_("Нельзя указывать даты получения и окончания сертификата, если тип сертификата 'В процессе'."))

        if self.certificate_type != 'В процессе':
            if not self.issue_date or not self.expiration_date:
                raise ValidationError(_("Для этого типа сертификата необходимо указать даты получения и окончания."))

        if self.pk:
            original = CertifiedCompany.objects.get(pk=self.pk)
            if original.certificate_type == 'Приостановлено' and self.certificate_type != 'Приостановлено':
                raise ValidationError(_("Нельзя изменить тип сертификата с 'Приостановлено' на другой."))

    def save(self, *args, **kwargs):
        self.update_certificate_type()
        self.full_clean()
        super().save(*args, **kwargs)

    def get_certificate_status_icon(self):
        if self.certificate_type == 'Сертифицированный':
            return f'https://{settings.SITE_DOMEN}{settings.MEDIA_URL}CertificateStatusIcon/Verified.png'
        elif self.certificate_type == 'В процессе':
            return f'https://{settings.SITE_DOMEN}{settings.MEDIA_URL}CertificateStatusIcon/In_progress.png'
        elif self.certificate_type == 'Приостановлено':
            return f'https://{settings.SITE_DOMEN}{settings.MEDIA_URL}CertificateStatusIcon/Suspended.png'
        elif self.certificate_type == 'Истекший':
            return f'https://{settings.SITE_DOMEN}{settings.MEDIA_URL}CertificateStatusIcon/Expired.png'

    def get_certificate_status_text(self):
        if self.certificate_type == 'Сертифицированный':
            return _('Проверенный Сертифицировано до')
        elif self.certificate_type == 'В процессе':
            return _('В процессе')
        elif self.certificate_type == 'Приостановлено':
            return _('Приостановлено')
        elif self.certificate_type == 'Истекший':
            return _('Истекший')

    class Meta:
        verbose_name = _('Сертифицированная компания')
        verbose_name_plural = _('Сертифицированные компании')
