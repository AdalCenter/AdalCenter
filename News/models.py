from django.db import models


class News(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    latest_update_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    address = models.CharField(max_length=255, verbose_name='Адрес', default='')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', default='')
    main_photo = models.ImageField(upload_to='NewsMainImage/%Y/%m/%d/', verbose_name='Главное фото новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsPhoto(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новости', related_name='photos')
    photo = models.ImageField(upload_to='news_images/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return f"{self.news.title} - {self.photo.url}"

    class Meta:
        verbose_name = 'Фото новостей'
        verbose_name_plural = 'Фото новостей'
