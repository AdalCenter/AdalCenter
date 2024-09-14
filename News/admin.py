from django.contrib import admin
from .models import *


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsPhotoInline]

admin.site.register(News, NewsAdmin)
admin.site.register(NewsPhoto)
