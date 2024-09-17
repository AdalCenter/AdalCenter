from django.contrib import admin
from .models import ECode, CodeType, TypeOfOrigin

@admin.register(ECode)
class ECodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'code_name', 'code_status', 'mini_description')
    search_fields = ('code', 'code_name', 'code_status')
    list_filter = ('code_status', 'code_type', 'type_of_origin')

@admin.register(CodeType)
class CodeTypeAdmin(admin.ModelAdmin):
    list_display = ('code_type',)
    search_fields = ('code_type',)

@admin.register(TypeOfOrigin)
class TypeOfOriginAdmin(admin.ModelAdmin):
    list_display = ('type_of_origin',)
    search_fields = ('type_of_origin',)
