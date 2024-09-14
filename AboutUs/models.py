from django.db import models


# Контакты и соц.сети
class Contact(models.Model):
    title = models.CharField(max_length=24)
    value = models.TextField()

    def __str__(self) -> str:
        return self.title

# Адрес
class Locate(models.Model):
    title = models.CharField(max_length=24)
    address = models.TextField()

    def __str__(self) -> str:
        return self.address

# Координаты филиалов офисов и.т.д
class Coordinate(models.Model):
    id = models.AutoField(primary_key=True)
    coordinate_title = models.CharField(max_length=255)
    x = models.FloatField()
    y = models.FloatField()
    url_title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.coordinate_title

# Партнеры
class Partners(models.Model):
    logo = models.ImageField(upload_to='PartnerLogo/')
    url = models.URLField()

    def __str__(self) -> str:
        return self.logo.url

# О нас
class AboutUs(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    image = models.ImageField(upload_to='AboutUs_images/')

    def __str__(self) -> str:
        return self.title

# Наши достижения
class OurAchievement(models.Model):
    title = models.CharField(max_length=36)
    text = models.TextField()
    icon = models.ImageField(upload_to='OurAchievement_icon/')

    def __str__(self) -> str:
        return self.title

# Наши цели и задачи
class OurGoalsAndObjectives(models.Model):
    title = models.CharField(max_length=24)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title

# Сертификаты
class OurAchievementCertificateImage(models.Model):
    image = models.ImageField(upload_to='Certificates_image/')

    def __str__(self) -> str:
        return self.image.url

# Сотрудники
class OurTeam(models.Model):
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34, blank=True, null=True)
    image = models.ImageField(upload_to='TeamPeople_Icon/')
    speciality = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} - {self.last_name}'

# Часто задаваемые вопросы
class FAQ(models.Model):
    title = models.CharField(max_length=100)
#    icon = models.ImageField(upload_to='FAQ_Icon/')
    text = models.TextField()

    def __str__(self) -> str:
        return self.title

# Запрещенные продукты
class BlackListCompanies(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='BlackListCompany/')
