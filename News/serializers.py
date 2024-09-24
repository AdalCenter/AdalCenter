from rest_framework import serializers
from .models import News, NewsPhoto


class NewsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPhoto
        fields = ['photo']


class NewsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'latest_update_date', 'create_date', 'address', 'title', 'main_photo', 'subtitle', 'description', 'images']
        extra_kwargs = {
            'id': {'help_text': 'Уникальный идентификатор новости'},
            'address': {'help_text': 'Адрес, связанный с новостью'},
            'title': {'help_text': 'Заголовок новости'},
            'subtitle': {'help_text': 'Подзаголовок новости'},
            'description': {'help_text': 'Полное описание новости'},
            'images': {'help_text': 'Список изображений, связанных с новостью'},
            'main_photo': {'help_text': 'Главное фото новости'},
            'latest_update_date': {'help_text': 'Дата последнего обновления новости'},
            'create_date': {'help_text': 'Дата создания новости'},
        }

    def get_images(self, obj):
        return [self.context['request'].build_absolute_uri(photo.photo.url) for photo in obj.photos.all()]
