# Generated by Django 5.0.8 on 2024-10-02 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название блока')),
                ('title_ru', models.CharField(max_length=60, null=True, verbose_name='Название блока')),
                ('title_en', models.CharField(max_length=60, null=True, verbose_name='Название блока')),
                ('title_ky', models.CharField(max_length=60, null=True, verbose_name='Название блока')),
                ('text', models.TextField(verbose_name='Описание о нас')),
                ('text_ru', models.TextField(null=True, verbose_name='Описание о нас')),
                ('text_en', models.TextField(null=True, verbose_name='Описание о нас')),
                ('text_ky', models.TextField(null=True, verbose_name='Описание о нас')),
                ('image', models.ImageField(upload_to='AboutUs_images/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Название адреса')),
                ('title_ru', models.CharField(max_length=24, null=True, verbose_name='Название адреса')),
                ('title_en', models.CharField(max_length=24, null=True, verbose_name='Название адреса')),
                ('title_ky', models.CharField(max_length=24, null=True, verbose_name='Название адреса')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('address_ru', models.TextField(null=True, verbose_name='Адрес')),
                ('address_en', models.TextField(null=True, verbose_name='Адрес')),
                ('address_ky', models.TextField(null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Boycott',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='BlackListCompany/', verbose_name='Фото компании')),
            ],
            options={
                'verbose_name': 'Байкот',
                'verbose_name_plural': 'Байкоты',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='ClientLogo/', verbose_name='Логотип')),
                ('url', models.URLField(verbose_name='Ссылка на клиента')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Название контакта')),
                ('title_ru', models.CharField(max_length=24, null=True, verbose_name='Название контакта')),
                ('title_en', models.CharField(max_length=24, null=True, verbose_name='Название контакта')),
                ('title_ky', models.CharField(max_length=24, null=True, verbose_name='Название контакта')),
                ('value', models.TextField(verbose_name='Контакт')),
                ('value_ru', models.TextField(null=True, verbose_name='Контакт')),
                ('value_en', models.TextField(null=True, verbose_name='Контакт')),
                ('value_ky', models.TextField(null=True, verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Вопрос')),
                ('title_ru', models.TextField(null=True, verbose_name='Вопрос')),
                ('title_en', models.TextField(null=True, verbose_name='Вопрос')),
                ('title_ky', models.TextField(null=True, verbose_name='Вопрос')),
                ('text', models.TextField(verbose_name='Ответ')),
                ('text_ru', models.TextField(null=True, verbose_name='Ответ')),
                ('text_en', models.TextField(null=True, verbose_name='Ответ')),
                ('text_ky', models.TextField(null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='MainPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=13, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Номер в главном',
                'verbose_name_plural': 'Номер в главном',
            },
        ),
        migrations.CreateModel(
            name='MobileAppUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(upload_to='QrCodeOurApp/', verbose_name='Qr-код на мобильного приложения ')),
                ('google_play', models.URLField(verbose_name='GooglePlayUrl')),
                ('app_store', models.URLField(verbose_name='AppStoreUrl')),
            ],
            options={
                'verbose_name': 'Ссылка на наше мобильное приложение',
                'verbose_name_plural': 'Ссылки на наши мобильные приложение',
            },
        ),
        migrations.CreateModel(
            name='OurAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36, verbose_name='Название достижения')),
                ('title_ru', models.CharField(max_length=36, null=True, verbose_name='Название достижения')),
                ('title_en', models.CharField(max_length=36, null=True, verbose_name='Название достижения')),
                ('title_ky', models.CharField(max_length=36, null=True, verbose_name='Название достижения')),
                ('text', models.TextField(verbose_name='Описание достижения')),
                ('text_ru', models.TextField(null=True, verbose_name='Описание достижения')),
                ('text_en', models.TextField(null=True, verbose_name='Описание достижения')),
                ('text_ky', models.TextField(null=True, verbose_name='Описание достижения')),
                ('icon', models.ImageField(upload_to='OurAchievement_icon/', verbose_name='Иконка достижения')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='OurAchievementCertificateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Certificates_image/', verbose_name='Фото нашего сертификата')),
            ],
            options={
                'verbose_name': 'НАш сертификат',
                'verbose_name_plural': 'Наши сертификаты',
            },
        ),
        migrations.CreateModel(
            name='OurGoalsAndObjectives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Название цели/задачи')),
                ('title_ru', models.CharField(max_length=24, null=True, verbose_name='Название цели/задачи')),
                ('title_en', models.CharField(max_length=24, null=True, verbose_name='Название цели/задачи')),
                ('title_ky', models.CharField(max_length=24, null=True, verbose_name='Название цели/задачи')),
                ('text', models.TextField(verbose_name='Описание цели/задачи')),
                ('text_ru', models.TextField(null=True, verbose_name='Описание цели/задачи')),
                ('text_en', models.TextField(null=True, verbose_name='Описание цели/задачи')),
                ('text_ky', models.TextField(null=True, verbose_name='Описание цели/задачи')),
            ],
            options={
                'verbose_name': 'Цель и задача',
                'verbose_name_plural': 'Цели и задачи',
            },
        ),
        migrations.CreateModel(
            name='OurIndicators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_foundation', models.TextField(verbose_name='Год основания')),
                ('number_of_domestic_enterprises', models.TextField(verbose_name='Количество отечественных предприятий')),
                ('number_offoreign_enterprises', models.TextField(verbose_name='Количество иностранных предприятий')),
                ('number_of_professionals', models.TextField(verbose_name='Количество профессионалов')),
            ],
            options={
                'verbose_name': 'Показатель',
                'verbose_name_plural': 'Показатели',
            },
        ),
        migrations.CreateModel(
            name='OurSites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='OurSitesIcon/', verbose_name='Иконка сайта')),
                ('site_name', models.CharField(max_length=22, verbose_name='Название сайта')),
                ('site_url', models.URLField(verbose_name='URL сайта')),
            ],
            options={
                'verbose_name': 'Наш сайт',
                'verbose_name_plural': 'Наши сайты',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=34, verbose_name='Имя')),
                ('first_name_ru', models.CharField(max_length=34, null=True, verbose_name='Имя')),
                ('first_name_en', models.CharField(max_length=34, null=True, verbose_name='Имя')),
                ('first_name_ky', models.CharField(max_length=34, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия')),
                ('last_name_ru', models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия')),
                ('last_name_en', models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия')),
                ('last_name_ky', models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия')),
                ('image', models.ImageField(upload_to='TeamPeople_Icon/', verbose_name='Фото')),
                ('speciality', models.TextField(verbose_name='Специализация')),
                ('speciality_ru', models.TextField(null=True, verbose_name='Специализация')),
                ('speciality_en', models.TextField(null=True, verbose_name='Специализация')),
                ('speciality_ky', models.TextField(null=True, verbose_name='Специализация')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Команда',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='PartnerLogo/', verbose_name='Логотип')),
                ('url', models.URLField(verbose_name='Ссылка на партнера')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='ProcessOfObtainingCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=22, verbose_name='Название или номер этапа')),
                ('description', models.TextField(verbose_name='Описание этапа')),
                ('icon', models.ImageField(upload_to='ProcessOfObtainingCertificateIcon/', verbose_name='Иконка этапа')),
                ('background_image', models.ImageField(upload_to='ProcessOfObtainingCertificateBackgroundImage/', verbose_name='Фоновое изображение этапа')),
            ],
            options={
                'verbose_name': 'Процесс получения сертификата',
                'verbose_name_plural': 'Процессы получения сертификатов',
            },
        ),
        migrations.CreateModel(
            name='RatingAndHowYouHeardAboutOurSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveSmallIntegerField(default=0, verbose_name='Оценка в звездах')),
                ('social_network', models.CharField(max_length=9, verbose_name='Социальная сеть')),
            ],
            options={
                'verbose_name': 'Оценка и рейтинг',
                'verbose_name_plural': 'Оценки и рейтинг',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='ProfilePhoto/', verbose_name='Фото профиля')),
                ('fullname', models.CharField(max_length=26, verbose_name='Ф.И.О')),
                ('fullname_ru', models.CharField(max_length=26, null=True, verbose_name='Ф.И.О')),
                ('fullname_en', models.CharField(max_length=26, null=True, verbose_name='Ф.И.О')),
                ('fullname_ky', models.CharField(max_length=26, null=True, verbose_name='Ф.И.О')),
                ('company_and_position_in_it', models.TextField(verbose_name='Компания и должность в ней')),
                ('company_and_position_in_it_ru', models.TextField(null=True, verbose_name='Компания и должность в ней')),
                ('company_and_position_in_it_en', models.TextField(null=True, verbose_name='Компания и должность в ней')),
                ('company_and_position_in_it_ky', models.TextField(null=True, verbose_name='Компания и должность в ней')),
                ('text', models.TextField(verbose_name='Содержимое отзыва')),
                ('text_ru', models.TextField(null=True, verbose_name='Содержимое отзыва')),
                ('text_en', models.TextField(null=True, verbose_name='Содержимое отзыва')),
                ('text_ky', models.TextField(null=True, verbose_name='Содержимое отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='SocialNetworkIcon/', verbose_name='Иконка социальной сети')),
                ('url', models.TextField(verbose_name='Ссылка на социальную сеть')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='SuggestionsOrComplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_qr_code', models.ImageField(upload_to='SuggestionsOrComplaintsTelegramQrCode/', verbose_name='Qr-код для жалоб и предложений Telegram')),
                ('whatsapp_qr_code', models.ImageField(upload_to='SuggestionsOrComplaintsWhatsAppQrCode/', verbose_name='Qr-код для жалоб и предложений WhatsApp')),
                ('whatsapp_url', models.URLField(verbose_name='URL для жалоб и предложений WhatsApp')),
                ('telegram_url', models.URLField(verbose_name='URL для жалоб и предложений Telegram')),
            ],
            options={
                'verbose_name': 'WhatsApp и Telegram для жалоб и предложений',
                'verbose_name_plural': 'WhatsApp и Telegram для жалоб и предложений',
            },
        ),
    ]
