from django.contrib import admin
from .models import News, NewsPhoto

class NewsPhotoInline(admin.TabularInline):
    model = NewsPhoto
    extra = 1  

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'latest_update_date')
    search_fields = ('title', 'description')
    list_filter = ('create_date',)
    inlines = [NewsPhotoInline]

admin.site.register(News, NewsAdmin)
