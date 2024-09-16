from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название контакта')
    value = models.TextField(verbose_name='Контакт')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакт'

class Address(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название адреса')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адрес'

class Partner(models.Model):
    logo = models.ImageField(upload_to='PartnerLogo/', verbose_name='Логотип')
    url = models.URLField(verbose_name='Ссылка на партнеров')

    def __str__(self) -> str:
        return self.logo.url

    class Meta:
        verbose_name = 'Наши партнеры'
        verbose_name_plural = 'Наш портнер'

class Client(models.Model):
    logo = models.ImageField(upload_to='ClientLogo/', verbose_name='Логотип')
    url = models.URLField(verbose_name='Ссылка на партнеров')

    def __str__(self) -> str:
        return self.logo.url

    class Meta:
        verbose_name = 'Наши клиенты'
        verbose_name_plural = 'Наш клиент'

class AboutUs(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название блока')
    text = models.TextField(verbose_name='Описание о нас')
    image = models.ImageField(upload_to='AboutUs_images/', verbose_name='Фото')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'О Нас'
        verbose_name_plural = 'О Нас'

class OurAchievement(models.Model):
    title = models.CharField(max_length=36, verbose_name='Названия достижения')
    text = models.TextField(verbose_name='Описание достижения')
    icon = models.ImageField(upload_to='OurAchievement_icon/', verbose_name='Иконка достижения')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Наши достижения'
        verbose_name_plural = 'Наше достижение'

class OurAchievementCertificateImage(models.Model):
    image = models.ImageField(upload_to='Certificates_image/', verbose_name='фото сертификата')

    def __str__(self) -> str:
        return self.image.url

    class Meta:
        verbose_name = 'Сертификаты наших достижений'
        verbose_name_plural = 'Сертификат них достижений'

class OurGoalsAndObjectives(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название Цели/Задачи')
    text = models.TextField(verbose_name='Описание наших целей/задач')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Наши цели и задачи'
        verbose_name_plural = 'Наша цель/задача'

class OurTeam(models.Model):
    first_name = models.CharField(max_length=34, verbose_name='Имя')
    last_name = models.CharField(max_length=34, blank=True, null=True, verbose_name='фамилия')
    image = models.ImageField(upload_to='TeamPeople_Icon/', verbose_name='фото')
    speciality = models.TextField(verbose_name='Специализация')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name or ""}'.strip()

    class Meta:
        verbose_name = 'Наша команда'
        verbose_name_plural = 'Сотрудник'

class FAQ(models.Model):
    title = models.TextField(verbose_name='Вопрос')
    text = models.TextField(verbose_name='Ответ')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемый вопрос'

class Boycott(models.Model):
    company_logo = models.ImageField(upload_to='BlackListCompany/', verbose_name='Фото компании')

    def __str__(self) -> str:
        return self.company_logo.url

    class Meta:
        verbose_name = 'Байкоты'
        verbose_name_plural = 'Байкот'

class Review(models.Model):
    name = models.CharField(max_length=18, verbose_name='Имя')
    stars = models.CharField(max_length=1, verbose_name='Кол-во звезд')
    text = models.TextField(verbose_name='Содержимое отзыва')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'

class ProcessOfObtainingCertificate(models.Model):
    title = models.CharField(max_length=22, verbose_name='Назвние или номер этапа')
    description = models.TextField(verbose_name='Описание этапа')
    icon = models.ImageField(upload_to='ProcessOfObtainingCertificateIcon/')
    backgrount_image = models.ImageField(upload_to='ProcessOfObtainingCertificateBackgroundImage/')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'ПРОЦЕССЫ ПОЛУЧЕНИЯ СЕРТИФИКАТА “ADAL CENTER”'
        verbose_name_plural = 'ПРОЦЕСС ПОЛУЧЕНИЯ СЕРТИФИКАТА “ADAL CENTER”'

class OurIndicators(models.Model):
    description = models.TextField(verbose_name='Наши показатели')

    def __str__(self) -> str:
        return self.description
    
    class Meta:
        verbose_name = 'Наши показатели'
        verbose_name_plural = 'Показатель'

class RatingAndHowYouHeardAboutOurSite(models.Model):
    stars = models.CharField(max_length=1, verbose_name='Оценка в звездах')
    social_network = models.CharField(max_length=9, verbose_name='Наши показатели')

    def __str__(self) -> str:
        return f"{self.social_network} - {self.stars}"

    class Meta:
        verbose_name = 'Статистики'
        verbose_name_plural = 'Статистика'

class SocialNetwork(models.Model):
    icon = models.ImageField(upload_to='SocialNetworkIcon/', verbose_name='Иконка социальной сети')
    url = models.TextField(verbose_name='Поле для ввода ссылки, номера и.д.т')

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальная сеть'
