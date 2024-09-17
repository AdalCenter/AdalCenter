from django.contrib import admin
from .models import ECode

@admin.register(ECode)
class ECodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'code_name', 'code_status')
    search_fields = ('code', 'code_name', 'code_status')
    list_filter = ('code_status',)
