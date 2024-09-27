from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    title = models.CharField(max_length=24, verbose_name=_('Название контакта'))
    value = models.TextField(verbose_name=_('Контакт'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')

class Address(models.Model):
    title = models.CharField(max_length=24, verbose_name=_('Название адреса'))
    address = models.TextField(verbose_name=_('Адрес'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')

class Partner(models.Model):
    logo = models.ImageField(upload_to='PartnerLogo/', verbose_name=_('Логотип'))
    url = models.URLField(verbose_name=_('Ссылка на партнера'))

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = _('Партнер')
        verbose_name_plural = _('Партнеры')

class Client(models.Model):
    logo = models.ImageField(upload_to='ClientLogo/', verbose_name=_('Логотип'))
    url = models.URLField(verbose_name=_('Ссылка на клиента'))

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

class AboutUs(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('Название блока'))
    text = models.TextField(verbose_name=_('Описание о нас'))
    image = models.ImageField(upload_to='AboutUs_images/', verbose_name=_('Фото'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')

class OurAchievement(models.Model):
    title = models.CharField(max_length=36, verbose_name=_('Название достижения'))
    text = models.TextField(verbose_name=_('Описание достижения'))
    icon = models.ImageField(upload_to='OurAchievement_icon/', verbose_name=_('Иконка достижения'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Достижение')
        verbose_name_plural = _('Достижения')

class OurAchievementCertificateImage(models.Model):
    image = models.ImageField(upload_to='Certificates_image/', verbose_name=_('Фото нашего сертификата'))

    def __str__(self) -> str:
        return self.image.url

    class Meta:
        verbose_name = _('Наш сертификат')
        verbose_name_plural = _('Наши сертификаты')

class OurGoalsAndObjectives(models.Model):
    title = models.CharField(max_length=24, verbose_name=_('Название цели/задачи'))
    text = models.TextField(verbose_name=_('Описание цели/задачи'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Цель и задача')
        verbose_name_plural = _('Цели и задачи')

class OurTeam(models.Model):
    first_name = models.CharField(max_length=34, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=34, blank=True, null=True, verbose_name=_('Фамилия'))
    image = models.ImageField(upload_to='TeamPeople_Icon/', verbose_name=_('Фото'))
    speciality = models.TextField(verbose_name=_('Специализация'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name or ""}'.strip()

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Команда')

class FAQ(models.Model):
    title = models.TextField(verbose_name=_('Вопрос'))
    text = models.TextField(verbose_name=_('Ответ'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Часто задаваемые вопросы')

class Boycott(models.Model):
    company_logo = models.ImageField(upload_to='BlackListCompany/', verbose_name=_('Фото компании'))

    def __str__(self) -> str:
        return self.company_logo.url

    class Meta:
        verbose_name = _('Байкот')
        verbose_name_plural = _('Байкоты')

class Review(models.Model):
    profile_photo = models.ImageField(upload_to='ProfilePhoto/', verbose_name=_('Фото профиля'))
    fullname = models.CharField(max_length=26, verbose_name=_('Ф.И.О'))
    company_and_position_in_it = models.TextField(verbose_name=_('Компания и должность в ней'))
    text = models.TextField(verbose_name=_('Содержимое отзыва'))

    def __str__(self) -> str:
        return self.fullname

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

class ProcessOfObtainingCertificate(models.Model):
    title = models.CharField(max_length=22, verbose_name=_('Название или номер этапа'))
    description = models.TextField(verbose_name=_('Описание этапа'))
    icon = models.ImageField(upload_to='ProcessOfObtainingCertificateIcon/', verbose_name=_('Иконка этапа'))
    background_image = models.ImageField(upload_to='ProcessOfObtainingCertificateBackgroundImage/', verbose_name=_('Фоновое изображение этапа'))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Процесс получения сертификата')
        verbose_name_plural = _('Процессы получения сертификатов')

class OurIndicators(models.Model):
    year_of_foundation = models.TextField(verbose_name=_('Год основания'))
    number_of_domestic_enterprises = models.TextField(verbose_name=_('Количество отечественных предприятий'))
    number_offoreign_enterprises = models.TextField(verbose_name=_('Количество иностранных предприятий'))
    number_of_professionals = models.TextField(verbose_name=_('Количество профессионалов'))

    def __str__(self) -> str:
        return f'Год основания: {self.year_of_foundation} - Количество отечественных предприятий: {self.number_of_domestic_enterprises} - Количество иностранных предприятий: {self.number_offoreign_enterprises} - Количество профессионалов: {self.number_of_professionals}'

    class Meta:
        verbose_name = _('Показатель')
        verbose_name_plural = _('Показатели')

class RatingAndHowYouHeardAboutOurSite(models.Model):
    stars = models.PositiveSmallIntegerField(default=0, verbose_name=_('Оценка в звездах'))
    social_network = models.CharField(max_length=9, verbose_name=_('Социальная сеть'))

    def __str__(self) -> str:
        return f"{self.social_network} - {self.stars}"

    class Meta:
        verbose_name = _('Оценка и рейтинг')
        verbose_name_plural = _('Оценки и рейтинг')

class SocialNetwork(models.Model):
    icon = models.ImageField(upload_to='SocialNetworkIcon/', verbose_name=_('Иконка социальной сети'))
    url = models.TextField(verbose_name=_('Ссылка на социальную сеть'))

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = _('Социальная сеть')
        verbose_name_plural = _('Социальные сети')

class MainPhoneNumber(models.Model):
    number = models.CharField(max_length=9, verbose_name=_('Номер телефона'))

    def __str__(self) -> str:
        return self.number

    class Meta:
        verbose_name = _('Номер в главном')
        verbose_name_plural = _('Номер в главном')

class OurSites(models.Model):
    icon = models.ImageField(upload_to='OurSitesIcon/', verbose_name=_('Иконка сайта'))
    site_name = models.CharField(max_length=22, verbose_name=_('Название сайта'))
    site_url = models.URLField(verbose_name=_('URL сайта'))

    def __str__(self) -> str:
        return self.site_name

    class Meta:
        verbose_name = _('Наш сайт')
        verbose_name_plural = _('Наши сайты')

class MobileAppUrl(models.Model):
    qr_code = models.ImageField(upload_to='QrCodeOurApp/', verbose_name=_('Qr-код на мобильного приложения '))
    google_play = models.URLField(verbose_name=_('GooglePlayUrl'))
    app_store = models.URLField(verbose_name=_('AppStoreUrl'))

    def __str__(self) -> str:
        return self.qr_code.url

    class Meta:
        verbose_name = _('Ссылка на наше мобильное приложение')
        verbose_name_plural = _('Ссылки на наши мобильные приложение')

class SuggestionsOrComplaints(models.Model):
    telegram_qr_code = models.ImageField(upload_to='SuggestionsOrComplaintsTelegramQrCode/', verbose_name=_('Qr-код для жалоб и предложений Telegram'))
    whatsapp_qr_code = models.ImageField(upload_to='SuggestionsOrComplaintsWhatsAppQrCode/', verbose_name=_('Qr-код для жалоб и предложений WhatsApp'))
    whatsapp_url = models.URLField(verbose_name=_('URL для жалоб и предложений WhatsApp'))
    telegram_url = models.URLField(verbose_name=_('URL для жалоб и предложений Telegram'))

    def __str__(self) -> str:
        return f"WhatsApp: {self.whatsapp_url} - Telegram: {self.telegram_url}"

    class Meta:
        verbose_name = _('WhatsApp и Telegram для жалоб и предложений')
        verbose_name_plural = _('WhatsApp и Telegram для жалоб и предложений')
