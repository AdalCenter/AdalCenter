from django.db import models


# Контакты и соц.сети
class Contact(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название контакта')
    value = models.TextField(verbose_name='Контакт')

    def __str__(self) -> str:
        return self.title

# Адрес
class Address(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название адреса')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self) -> str:
        return f"{self.title}"

# Партнеры
class Partner(models.Model):
    logo = models.ImageField(upload_to='PartnerLogo/', verbose_name='Логотип')
    url = models.URLField(verbose_name='Ссылка на партнеров')

    def __str__(self) -> str:
        return self.logo.url

# О нас
class AboutUs(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название блока')
    text = models.TextField(verbose_name='Описание о нас')
    image = models.ImageField(upload_to='AboutUs_images/', verbose_name='Фото')

    def __str__(self) -> str:
        return self.title

# Наши достижения
class OurAchievement(models.Model):
    title = models.CharField(max_length=36, verbose_name='Названия достижения')
    text = models.TextField(verbose_name='Описание достижения')
    icon = models.ImageField(upload_to='OurAchievement_icon/', verbose_name='Иконка достижения')

    def __str__(self) -> str:
        return self.title

# Наши цели и задачи
class OurGoalsAndObjectives(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название Цели/Задачи')
    text = models.TextField(verbose_name='Описание наших целей/задач')

    def __str__(self) -> str:
        return self.title

# Сертификаты
class OurAchievementCertificateImage(models.Model):
    image = models.ImageField(upload_to='Certificates_image/', verbose_name='фото сертификата')

    def __str__(self) -> str:
        return self.image.url

# Сотрудники
class OurTeam(models.Model):
    first_name = models.CharField(max_length=34, verbose_name='Имя')
    last_name = models.CharField(max_length=34, blank=True, null=True, verbose_name='фамилия')
    image = models.ImageField(upload_to='TeamPeople_Icon/', verbose_name='фото')
    speciality = models.TextField(verbose_name='Специализация')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name or ""}'.strip()

# Часто задаваемые вопросы
class FAQ(models.Model):
    title = models.TextField(verbose_name='Вопрос')
    text = models.TextField(verbose_name='Ответ')

    def __str__(self) -> str:
        return self.title

# Запрещенные Компании
class BlackListCompany(models.Model):
    title = models.TextField(blank=True, null=True, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='BlackListCompany/', verbose_name='Фото компании')

    def __str__(self) -> str:
        return self.title or 'Без заголовка'

class Review(models.Model):
    name = models.CharField(max_length=18, verbose_name='Имя')
    stars = models.CharField(max_length=1, verbose_name='Кол-во звезд')
    text = models.TextField(verbose_name='Содержимое отзыва')

    def __str__(self) -> str:
        return self.name
