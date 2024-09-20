from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название контакта')
    value = models.TextField(verbose_name='Контакт')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Address(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название адреса')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Partner(models.Model):
    logo = models.ImageField(upload_to='PartnerLogo/', verbose_name='Логотип')
    url = models.URLField(verbose_name='Ссылка на партнера')

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Client(models.Model):
    logo = models.ImageField(upload_to='ClientLogo/', verbose_name='Логотип')
    url = models.URLField(verbose_name='Ссылка на клиента')

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class AboutUs(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название блока')
    text = models.TextField(verbose_name='Описание о нас')
    image = models.ImageField(upload_to='AboutUs_images/', verbose_name='Фото')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class OurAchievement(models.Model):
    title = models.CharField(max_length=36, verbose_name='Название достижения')
    text = models.TextField(verbose_name='Описание достижения')
    icon = models.ImageField(upload_to='OurAchievement_icon/', verbose_name='Иконка достижения')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class OurAchievementCertificateImage(models.Model):
    image = models.ImageField(upload_to='Certificates_image/', verbose_name='Фото сертификата')

    def __str__(self) -> str:
        return self.image.url

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class OurGoalsAndObjectives(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название цели/задачи')
    text = models.TextField(verbose_name='Описание цели/задачи')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Цель и задача'
        verbose_name_plural = 'Цели и задачи'


class OurTeam(models.Model):
    first_name = models.CharField(max_length=34, verbose_name='Имя')
    last_name = models.CharField(max_length=34, blank=True, null=True, verbose_name='Фамилия')
    image = models.ImageField(upload_to='TeamPeople_Icon/', verbose_name='Фото')
    speciality = models.TextField(verbose_name='Специализация')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name or ""}'.strip()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Команда'


class FAQ(models.Model):
    title = models.TextField(verbose_name='Вопрос')
    text = models.TextField(verbose_name='Ответ')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'


class Boycott(models.Model):
    company_logo = models.ImageField(upload_to='BlackListCompany/', verbose_name='Фото компании')

    def __str__(self) -> str:
        return self.company_logo.url

    class Meta:
        verbose_name = 'Байкот'
        verbose_name_plural = 'Байкоты'


class Review(models.Model):
    profile_photo = models.ImageField(upload_to='ProfilePhoto/', verbose_name='Фото профиля')
    fullname = models.CharField(max_length=26, verbose_name='Ф.И.О')
    company_and_position_in_it = models.TextField(verbose_name='Компания и должность в ней')
    text = models.TextField(verbose_name='Содержимое отзыва')

    def __str__(self) -> str:
        return self.fullname

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProcessOfObtainingCertificate(models.Model):
    title = models.CharField(max_length=22, verbose_name='Название или номер этапа')
    description = models.TextField(verbose_name='Описание этапа')
    icon = models.ImageField(upload_to='ProcessOfObtainingCertificateIcon/', verbose_name='Иконка этапа')
    background_image = models.ImageField(upload_to='ProcessOfObtainingCertificateBackgroundImage/', verbose_name='Фоновое изображение этапа')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Процесс получения сертификата'
        verbose_name_plural = 'Процессы получения сертификатов'


class OurIndicators(models.Model):
    year_of_foundation = models.TextField(verbose_name='Год основания')
    number_of_domestic_enterprises = models.TextField(verbose_name='Количество отечественных предприятий')
    number_offoreign_enterprises = models.TextField(verbose_name='Количество иностранных предприятий')
    number_of_professionals = models.TextField(verbose_name='Количество профессионалов')

    def __str__(self) -> str:
        return f'Год основания: {self.year_of_foundation} - Количество отечественных предприятий: {self.number_of_domestic_enterprises} - Количество иностранных предприятий: {self.number_offoreign_enterprises} - Количество профессионалов: {self.number_of_professionals}'

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'


class RatingAndHowYouHeardAboutOurSite(models.Model):
    stars = models.PositiveSmallIntegerField(default=0, verbose_name='Оценка в звездах')
    social_network = models.CharField(max_length=9, verbose_name='Социальная сеть')

    def __str__(self) -> str:
        return f"{self.social_network} - {self.stars}"

    class Meta:
        verbose_name = 'Оценка и рейтинг'
        verbose_name_plural = 'Оценки и рейтинг'

class SocialNetwork(models.Model):
    icon = models.ImageField(upload_to='SocialNetworkIcon/', verbose_name='Иконка социальной сети')
    url = models.TextField(verbose_name='Ссылка на социальную сеть')

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

class MainPhoneNumber(models.Model):
    number = models.CharField(max_length=9, verbose_name='Номер телефона')

    def __str__(self) -> str:
        return self.number

    class Meta:
        verbose_name = 'Номер в главном'
        verbose_name_plural = 'Номер в главном'

class OurSites(models.Model):
    icon = models.ImageField(upload_to='OurSitesIcon/', verbose_name='Иконка сайта')
    site_name = models.CharField(max_length=22, verbose_name='Название сайта')
    site_url = models.URLField(verbose_name='URL сайта')

    def __str__(self) -> str:
        return self.site_name

    class Meta:
        verbose_name = 'Наш сайт'
        verbose_name_plural = 'Наши сайты'

class MobileAppUrl(models.Model):
    qr_code = models.ImageField(upload_to='QrCodeOurApp/', verbose_name='Qr-код на мобильного приложения ')
    google_play = models.URLField(verbose_name='GooglePlayUrl')
    app_store = models.URLField(verbose_name='AppStoreUrl')

    def __str__(self) -> str:
        return self.qr_code.url

    class Meta:
        verbose_name = 'Ссылка на наше мобильное приложение'
        verbose_name_plural = 'Ссылки на наши мобильные приложение'

class SuggestionsOrComplaints(models.Model):
    telegram_qr_code = models.ImageField(upload_to='SuggestionsOrComplaintsTelegramQrCode/', verbose_name='Qr-код для жалоб и предложений Telegram')
    whatsapp_qr_code = models.ImageField(upload_to='SuggestionsOrComplaintsWhatsAppQrCode/', verbose_name='Qr-код для жалоб и предложений WhatsApp')
    whatsapp_url = models.URLField(verbose_name='URL для жалоб и предложений WhatsApp')
    telegram_url = models.URLField(verbose_name='URL для жалоб и предложений Telegram')

    def __str__(self) -> str:
        return f"WhatsApp: {self.whatsapp_url} - Telegram: {self.telegram_url}"

    class Meta:
        verbose_name = 'WhatsApp и Telegram для жалоб и предложений'
        verbose_name_plural = 'WhatsApp и Telegram для жалоб и предложений'
