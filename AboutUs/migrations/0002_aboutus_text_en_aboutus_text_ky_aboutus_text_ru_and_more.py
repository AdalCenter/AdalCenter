# Generated by Django 5.0.8 on 2024-09-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Описание о нас'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Описание о нас'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Описание о нас'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Название блока'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_ky',
            field=models.CharField(max_length=60, null=True, verbose_name='Название блока'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_ru',
            field=models.CharField(max_length=60, null=True, verbose_name='Название блока'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_en',
            field=models.TextField(null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_ky',
            field=models.TextField(null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_ru',
            field=models.TextField(null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='address',
            name='title_en',
            field=models.CharField(max_length=24, null=True, verbose_name='Название адреса'),
        ),
        migrations.AddField(
            model_name='address',
            name='title_ky',
            field=models.CharField(max_length=24, null=True, verbose_name='Название адреса'),
        ),
        migrations.AddField(
            model_name='address',
            name='title_ru',
            field=models.CharField(max_length=24, null=True, verbose_name='Название адреса'),
        ),
        migrations.AddField(
            model_name='boycott',
            name='company_logo_en',
            field=models.ImageField(null=True, upload_to='BlackListCompany/', verbose_name='Фото компании'),
        ),
        migrations.AddField(
            model_name='boycott',
            name='company_logo_ky',
            field=models.ImageField(null=True, upload_to='BlackListCompany/', verbose_name='Фото компании'),
        ),
        migrations.AddField(
            model_name='boycott',
            name='company_logo_ru',
            field=models.ImageField(null=True, upload_to='BlackListCompany/', verbose_name='Фото компании'),
        ),
        migrations.AddField(
            model_name='client',
            name='url_en',
            field=models.URLField(null=True, verbose_name='Ссылка на клиента'),
        ),
        migrations.AddField(
            model_name='client',
            name='url_ky',
            field=models.URLField(null=True, verbose_name='Ссылка на клиента'),
        ),
        migrations.AddField(
            model_name='client',
            name='url_ru',
            field=models.URLField(null=True, verbose_name='Ссылка на клиента'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_en',
            field=models.CharField(max_length=24, null=True, verbose_name='Название контакта'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ky',
            field=models.CharField(max_length=24, null=True, verbose_name='Название контакта'),
        ),
        migrations.AddField(
            model_name='contact',
            name='title_ru',
            field=models.CharField(max_length=24, null=True, verbose_name='Название контакта'),
        ),
        migrations.AddField(
            model_name='contact',
            name='value_en',
            field=models.TextField(null=True, verbose_name='Контакт'),
        ),
        migrations.AddField(
            model_name='contact',
            name='value_ky',
            field=models.TextField(null=True, verbose_name='Контакт'),
        ),
        migrations.AddField(
            model_name='contact',
            name='value_ru',
            field=models.TextField(null=True, verbose_name='Контакт'),
        ),
        migrations.AddField(
            model_name='faq',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='faq',
            name='title_en',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='faq',
            name='title_ky',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='faq',
            name='title_ru',
            field=models.TextField(null=True, verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='mainphonenumber',
            name='number_en',
            field=models.CharField(max_length=9, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='mainphonenumber',
            name='number_ky',
            field=models.CharField(max_length=9, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='mainphonenumber',
            name='number_ru',
            field=models.CharField(max_length=9, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='mobileappurl',
            name='app_store_en',
            field=models.URLField(null=True, verbose_name='AppStoreUrl'),
        ),
        migrations.AddField(
            model_name='mobileappurl',
            name='app_store_ky',
            field=models.URLField(null=True, verbose_name='AppStoreUrl'),
        ),
        migrations.AddField(
            model_name='mobileappurl',
            name='app_store_ru',
            field=models.URLField(null=True, verbose_name='AppStoreUrl'),
        ),
        migrations.AddField(
            model_name='mobileappurl',
            name='google_play_en',
            field=models.URLField(null=True, verbose_name='GooglePlayUrl'),
        ),
        migrations.AddField(
            model_name='mobileappurl',
            name='google_play_ky',
            field=models.URLField(null=True, verbose_name='GooglePlayUrl'),
        ),
        migrations.AddField(
            model_name='mobileappurl',
            name='google_play_ru',
            field=models.URLField(null=True, verbose_name='GooglePlayUrl'),
        ),
        migrations.AddField(
            model_name='ourachievement',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Описание достижения'),
        ),
        migrations.AddField(
            model_name='ourachievement',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Описание достижения'),
        ),
        migrations.AddField(
            model_name='ourachievement',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Описание достижения'),
        ),
        migrations.AddField(
            model_name='ourachievement',
            name='title_en',
            field=models.CharField(max_length=36, null=True, verbose_name='Название достижения'),
        ),
        migrations.AddField(
            model_name='ourachievement',
            name='title_ky',
            field=models.CharField(max_length=36, null=True, verbose_name='Название достижения'),
        ),
        migrations.AddField(
            model_name='ourachievement',
            name='title_ru',
            field=models.CharField(max_length=36, null=True, verbose_name='Название достижения'),
        ),
        migrations.AddField(
            model_name='ourgoalsandobjectives',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Описание цели/задачи'),
        ),
        migrations.AddField(
            model_name='ourgoalsandobjectives',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Описание цели/задачи'),
        ),
        migrations.AddField(
            model_name='ourgoalsandobjectives',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Описание цели/задачи'),
        ),
        migrations.AddField(
            model_name='ourgoalsandobjectives',
            name='title_en',
            field=models.CharField(max_length=24, null=True, verbose_name='Название цели/задачи'),
        ),
        migrations.AddField(
            model_name='ourgoalsandobjectives',
            name='title_ky',
            field=models.CharField(max_length=24, null=True, verbose_name='Название цели/задачи'),
        ),
        migrations.AddField(
            model_name='ourgoalsandobjectives',
            name='title_ru',
            field=models.CharField(max_length=24, null=True, verbose_name='Название цели/задачи'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_of_domestic_enterprises_en',
            field=models.TextField(null=True, verbose_name='Количество отечественных предприятий'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_of_domestic_enterprises_ky',
            field=models.TextField(null=True, verbose_name='Количество отечественных предприятий'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_of_domestic_enterprises_ru',
            field=models.TextField(null=True, verbose_name='Количество отечественных предприятий'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_of_professionals_en',
            field=models.TextField(null=True, verbose_name='Количество профессионалов'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_of_professionals_ky',
            field=models.TextField(null=True, verbose_name='Количество профессионалов'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_of_professionals_ru',
            field=models.TextField(null=True, verbose_name='Количество профессионалов'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_offoreign_enterprises_en',
            field=models.TextField(null=True, verbose_name='Количество иностранных предприятий'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_offoreign_enterprises_ky',
            field=models.TextField(null=True, verbose_name='Количество иностранных предприятий'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='number_offoreign_enterprises_ru',
            field=models.TextField(null=True, verbose_name='Количество иностранных предприятий'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='year_of_foundation_en',
            field=models.TextField(null=True, verbose_name='Год основания'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='year_of_foundation_ky',
            field=models.TextField(null=True, verbose_name='Год основания'),
        ),
        migrations.AddField(
            model_name='ourindicators',
            name='year_of_foundation_ru',
            field=models.TextField(null=True, verbose_name='Год основания'),
        ),
        migrations.AddField(
            model_name='oursites',
            name='site_name_en',
            field=models.CharField(max_length=22, null=True, verbose_name='Название сайта'),
        ),
        migrations.AddField(
            model_name='oursites',
            name='site_name_ky',
            field=models.CharField(max_length=22, null=True, verbose_name='Название сайта'),
        ),
        migrations.AddField(
            model_name='oursites',
            name='site_name_ru',
            field=models.CharField(max_length=22, null=True, verbose_name='Название сайта'),
        ),
        migrations.AddField(
            model_name='oursites',
            name='site_url_en',
            field=models.URLField(null=True, verbose_name='URL сайта'),
        ),
        migrations.AddField(
            model_name='oursites',
            name='site_url_ky',
            field=models.URLField(null=True, verbose_name='URL сайта'),
        ),
        migrations.AddField(
            model_name='oursites',
            name='site_url_ru',
            field=models.URLField(null=True, verbose_name='URL сайта'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='first_name_en',
            field=models.CharField(max_length=34, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='first_name_ky',
            field=models.CharField(max_length=34, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='first_name_ru',
            field=models.CharField(max_length=34, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='last_name_ky',
            field=models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='last_name_ru',
            field=models.CharField(blank=True, max_length=34, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='speciality_en',
            field=models.TextField(null=True, verbose_name='Специализация'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='speciality_ky',
            field=models.TextField(null=True, verbose_name='Специализация'),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='speciality_ru',
            field=models.TextField(null=True, verbose_name='Специализация'),
        ),
        migrations.AddField(
            model_name='partner',
            name='url_en',
            field=models.URLField(null=True, verbose_name='Ссылка на партнера'),
        ),
        migrations.AddField(
            model_name='partner',
            name='url_ky',
            field=models.URLField(null=True, verbose_name='Ссылка на партнера'),
        ),
        migrations.AddField(
            model_name='partner',
            name='url_ru',
            field=models.URLField(null=True, verbose_name='Ссылка на партнера'),
        ),
        migrations.AddField(
            model_name='processofobtainingcertificate',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание этапа'),
        ),
        migrations.AddField(
            model_name='processofobtainingcertificate',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='Описание этапа'),
        ),
        migrations.AddField(
            model_name='processofobtainingcertificate',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание этапа'),
        ),
        migrations.AddField(
            model_name='processofobtainingcertificate',
            name='title_en',
            field=models.CharField(max_length=22, null=True, verbose_name='Название или номер этапа'),
        ),
        migrations.AddField(
            model_name='processofobtainingcertificate',
            name='title_ky',
            field=models.CharField(max_length=22, null=True, verbose_name='Название или номер этапа'),
        ),
        migrations.AddField(
            model_name='processofobtainingcertificate',
            name='title_ru',
            field=models.CharField(max_length=22, null=True, verbose_name='Название или номер этапа'),
        ),
        migrations.AddField(
            model_name='ratingandhowyouheardaboutoursite',
            name='social_network_en',
            field=models.CharField(max_length=9, null=True, verbose_name='Социальная сеть'),
        ),
        migrations.AddField(
            model_name='ratingandhowyouheardaboutoursite',
            name='social_network_ky',
            field=models.CharField(max_length=9, null=True, verbose_name='Социальная сеть'),
        ),
        migrations.AddField(
            model_name='ratingandhowyouheardaboutoursite',
            name='social_network_ru',
            field=models.CharField(max_length=9, null=True, verbose_name='Социальная сеть'),
        ),
        migrations.AddField(
            model_name='review',
            name='company_and_position_in_it_en',
            field=models.TextField(null=True, verbose_name='Компания и должность в ней'),
        ),
        migrations.AddField(
            model_name='review',
            name='company_and_position_in_it_ky',
            field=models.TextField(null=True, verbose_name='Компания и должность в ней'),
        ),
        migrations.AddField(
            model_name='review',
            name='company_and_position_in_it_ru',
            field=models.TextField(null=True, verbose_name='Компания и должность в ней'),
        ),
        migrations.AddField(
            model_name='review',
            name='fullname_en',
            field=models.CharField(max_length=26, null=True, verbose_name='Ф.И.О'),
        ),
        migrations.AddField(
            model_name='review',
            name='fullname_ky',
            field=models.CharField(max_length=26, null=True, verbose_name='Ф.И.О'),
        ),
        migrations.AddField(
            model_name='review',
            name='fullname_ru',
            field=models.CharField(max_length=26, null=True, verbose_name='Ф.И.О'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Содержимое отзыва'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_ky',
            field=models.TextField(null=True, verbose_name='Содержимое отзыва'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Содержимое отзыва'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='url_en',
            field=models.TextField(null=True, verbose_name='Ссылка на социальную сеть'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='url_ky',
            field=models.TextField(null=True, verbose_name='Ссылка на социальную сеть'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='url_ru',
            field=models.TextField(null=True, verbose_name='Ссылка на социальную сеть'),
        ),
        migrations.AddField(
            model_name='suggestionsorcomplaints',
            name='telegram_url_en',
            field=models.URLField(null=True, verbose_name='URL для жалоб и предложений Telegram'),
        ),
        migrations.AddField(
            model_name='suggestionsorcomplaints',
            name='telegram_url_ky',
            field=models.URLField(null=True, verbose_name='URL для жалоб и предложений Telegram'),
        ),
        migrations.AddField(
            model_name='suggestionsorcomplaints',
            name='telegram_url_ru',
            field=models.URLField(null=True, verbose_name='URL для жалоб и предложений Telegram'),
        ),
        migrations.AddField(
            model_name='suggestionsorcomplaints',
            name='whatsapp_url_en',
            field=models.URLField(null=True, verbose_name='URL для жалоб и предложений WhatsApp'),
        ),
        migrations.AddField(
            model_name='suggestionsorcomplaints',
            name='whatsapp_url_ky',
            field=models.URLField(null=True, verbose_name='URL для жалоб и предложений WhatsApp'),
        ),
        migrations.AddField(
            model_name='suggestionsorcomplaints',
            name='whatsapp_url_ru',
            field=models.URLField(null=True, verbose_name='URL для жалоб и предложений WhatsApp'),
        ),
    ]
