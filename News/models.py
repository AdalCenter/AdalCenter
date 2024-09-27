from django.db import models
from django.utils.translation import gettext_lazy as _

class News(models.Model):
    create_date = models.DateTimeField(verbose_name=_('Дата создания'))
    latest_update_date = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    address = models.CharField(max_length=255, verbose_name=_('Адрес'), default='')
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    subtitle = models.CharField(max_length=255, verbose_name=_('Подзаголовок'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Описание'), default='')
    main_photo = models.ImageField(upload_to='NewsMainImage/%Y/%m/%d/', verbose_name=_('Главное фото новости'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')


class NewsPhoto(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('Новости'), related_name='photos')
    photo = models.ImageField(upload_to='news_images/%Y/%m/%d/', verbose_name=_('Фото'))

    def __str__(self):
        return f"{self.news.title} - {self.photo.url}"

    class Meta:
        verbose_name = _('Фото новостей')
        verbose_name_plural = _('Фото новостей')
