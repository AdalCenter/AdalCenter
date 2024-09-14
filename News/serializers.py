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
        fields = ['id', 'date', 'address', 'title', 'subtitle', 'description', 'images']

    def get_images(self, obj):
        return [self.context['request'].build_absolute_uri(photo.photo.url) for photo in obj.photos.all()]
