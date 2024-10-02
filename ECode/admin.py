from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ECode


@admin.register(ECode)
class ECodeAdmin(TranslationAdmin):
    list_display = ('code', 'code_name', 'code_status', 'description')
    search_fields = ('code', 'code_name')
    list_filter = ('code_status',)
