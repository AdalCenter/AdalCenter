from django.contrib import admin
from .models import ECode
from modeltranslation.admin import TranslationAdmin


@admin.register(ECode)
class ECodeAdmin(TranslationAdmin):
    list_display = ('code', 'code_name', 'code_status')
    search_fields = ('code', 'code_name', 'code_status')
    list_filter = ('code_status',)
