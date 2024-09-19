from django.db import models
import qrcode
from django.core.files import File
from io import BytesIO
from django.conf import settings


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
    issue_date = models.DateTimeField(verbose_name="Дата и время получения сертификата")
    expiration_date = models.DateTimeField(verbose_name="Дата и время окончания сертификата")
    certificate_type = models.CharField(max_length=50, choices=[('Сертифицированный', 'Сертифицированный'), ('В процессе', 'В процессе'), ('Приостановлено', 'Приостановлено'), ('Истекшие', 'Истекшие')], default='В процессе', verbose_name="Тип сертификата")

    def save(self, *args, **kwargs):
        if not self.qr_code and self.certificate_photo:
            download_url = f'https://{settings.SITE_DOMEN}{self.certificate_photo.url}'
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
            buffer.seek(0)
            self.qr_code.save(f'qr_{self.pk}.png', File(buffer), save=False)
            buffer.close()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Сертифицированная компания'
        verbose_name_plural = 'Сертифицированные компании'

import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.utils.encoding import smart_str

def download_certificate(request, filename):
    # Путь к директории, где хранятся файлы сертификатов
    file_path = os.path.join(settings.MEDIA_ROOT, 'company_photos', filename)
    
    # Проверка, существует ли файл
    if os.path.exists(file_path):
        # Открываем файл для чтения в бинарном режиме
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            # Добавляем заголовок для загрузки файла
            response['Content-Disposition'] = f'attachment; filename={smart_str(filename)}'
            return response
    else:
        # Если файл не найден, возвращаем 404 ошибку
        raise Http404("Файл не найден")
