from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, NewsPhoto


class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 1

class NewsAdmin(TranslationAdmin):
    inlines = [NewsPhotoInline]
    list_display = ('title', 'create_date', 'latest_update_date', 'address')
    search_fields = ('title', 'address')
    list_filter = ('create_date',)

admin.site.register(News, NewsAdmin)
admin.site.register(NewsPhoto)
