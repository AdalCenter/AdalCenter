# Generated by Django 5.0.8 on 2024-10-09 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Ф.И.О')),
                ('fullname_ru', models.CharField(max_length=255, null=True, verbose_name='Ф.И.О')),
                ('fullname_en', models.CharField(max_length=255, null=True, verbose_name='Ф.И.О')),
                ('fullname_ky', models.CharField(max_length=255, null=True, verbose_name='Ф.И.О')),
                ('observer_profile_image', models.ImageField(upload_to='ObserverProfileImage/', verbose_name='Фото профиля наблюдателя')),
                ('contact_number', models.CharField(max_length=50, verbose_name='Контактный номер')),
                ('contact_number_ru', models.CharField(max_length=50, null=True, verbose_name='Контактный номер')),
                ('contact_number_en', models.CharField(max_length=50, null=True, verbose_name='Контактный номер')),
                ('contact_number_ky', models.CharField(max_length=50, null=True, verbose_name='Контактный номер')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('address_ru', models.TextField(null=True, verbose_name='Адрес')),
                ('address_en', models.TextField(null=True, verbose_name='Адрес')),
                ('address_ky', models.TextField(null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Наблюдатель',
                'verbose_name_plural': 'Наблюдатели',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='service-images/', verbose_name='Фото какого-то сервиса')),
                ('service', models.CharField(max_length=64, unique=True, verbose_name='Тип обслуживания')),
                ('service_ru', models.CharField(max_length=64, null=True, unique=True, verbose_name='Тип обслуживания')),
                ('service_en', models.CharField(max_length=64, null=True, unique=True, verbose_name='Тип обслуживания')),
                ('service_ky', models.CharField(max_length=64, null=True, unique=True, verbose_name='Тип обслуживания')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
        migrations.CreateModel(
            name='CertifiedCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_email', models.EmailField(max_length=254, verbose_name='Электронная почта компании')),
                ('certificate_name', models.CharField(max_length=28, verbose_name='Название сертификата')),
                ('certificate_name_ru', models.CharField(max_length=28, null=True, verbose_name='Название сертификата')),
                ('certificate_name_en', models.CharField(max_length=28, null=True, verbose_name='Название сертификата')),
                ('certificate_name_ky', models.CharField(max_length=28, null=True, verbose_name='Название сертификата')),
                ('company_photo', models.ImageField(upload_to='company_photos/', verbose_name='Фото компании (внутри или снаружи)')),
                ('company_name', models.CharField(max_length=255, unique=True, verbose_name='Название компании')),
                ('company_name_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='Название компании')),
                ('company_name_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='Название компании')),
                ('company_name_ky', models.CharField(max_length=255, null=True, unique=True, verbose_name='Название компании')),
                ('trademark', models.CharField(max_length=255, unique=True, verbose_name='Товарный знак')),
                ('registration_number', models.CharField(max_length=100, unique=True, verbose_name='Регистрационный номер')),
                ('region', models.CharField(max_length=255, verbose_name='Область')),
                ('company_address', models.TextField(unique=True, verbose_name='Адрес компании')),
                ('certificate_photo', models.ImageField(upload_to='certificate_photos/', verbose_name='Фото сертификата')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/', verbose_name='QR-код')),
                ('issue_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и времени получения сертификата')),
                ('expiration_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и времени окончания сертификата')),
                ('certificate_type', models.CharField(choices=[('Сертифицированный', 'Сертифицированный'), ('В процессе', 'В процессе'), ('Приостановлено', 'Приостановлено'), ('Истекший', 'Истекший')], max_length=50, verbose_name='Тип сертификата')),
                ('observer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Certification.observer', verbose_name='Наблюдатель')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='Certification.service', verbose_name='Тип обслуживания')),
            ],
            options={
                'verbose_name': 'Сертифицированная компания',
                'verbose_name_plural': 'Сертифицированные компании',
            },
        ),
    ]
