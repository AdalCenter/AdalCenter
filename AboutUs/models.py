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
    name = models.CharField(max_length=18, verbose_name='Имя')
    stars = models.CharField(max_length=1, verbose_name='Количество звезд')
    text = models.TextField(verbose_name='Содержимое отзыва')

    def __str__(self) -> str:
        return self.name

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
    description = models.TextField(verbose_name='Описание показателя')

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'


class RatingAndHowYouHeardAboutOurSite(models.Model):
    stars = models.CharField(max_length=1, verbose_name='Оценка в звездах')
    social_network = models.CharField(max_length=9, verbose_name='Социальная сеть')

    def __str__(self) -> str:
        return f"{self.social_network} - {self.stars}"

    class Meta:
        verbose_name = 'Оценка и отзывы'
        verbose_name_plural = 'Оценки и отзывы'


class SocialNetwork(models.Model):
    icon = models.ImageField(upload_to='SocialNetworkIcon/', verbose_name='Иконка социальной сети')
    url = models.TextField(verbose_name='Ссылка на социальную сеть')

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
