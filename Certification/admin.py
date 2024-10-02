# #from django.contrib import admin
# #from django.core.exceptions import ValidationError
# #from django.utils.html import format_html
# #from .models import Observer, Service, CertifiedCompany

# #@admin.register(Observer)
# #class ObserverAdmin(admin.ModelAdmin):
# #    list_display = ('fullname', 'contact_number', 'address')
# #    search_fields = ('fullname', 'contact_number')

# #@admin.register(Service)
# #class ServiceAdmin(admin.ModelAdmin):
# #    list_display = ('service',)
# #    search_fields = ('service',)

# #@admin.register(CertifiedCompany)
# #class CertifiedCompanyAdmin(admin.ModelAdmin):
# #    list_display = ('company_name', 'trademark', 'registration_number', 'region', 'certificate_type')
# #    search_fields = ('company_name', 'trademark', 'registration_number')
# #    list_filter = ('certificate_type', 'service_type')

# #    def save_model(self, request, obj, form, change):
# #        try:
#             # Попытка сохранения модели с вызовом проверки (clean)
# #            obj.save()
# #        except ValidationError as e:
# #            # Если возникает ошибка валидации, отображаем её в форме
# #            form.add_error(None, format_html('<span style="color: red;">{}</span>', str(e)))
# from django.contrib import admin
# from django.core.exceptions import ValidationError
# from django.utils.html import format_html
# from .models import Observer, Service, CertifiedCompany

# @admin.register(Observer)
# class ObserverAdmin(admin.ModelAdmin):
#     list_display = ('fullname', 'contact_number', 'address')
#     search_fields = ('fullname', 'contact_number')

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('service',)
#     search_fields = ('service',)

# @admin.register(CertifiedCompany)
# class CertifiedCompanyAdmin(admin.ModelAdmin):
#     list_display = ('company_name', 'trademark', 'registration_number', 'region', 'certificate_type')
#     search_fields = ('company_name', 'trademark', 'registration_number')
#     list_filter = ('certificate_type', 'service_type')

#     def save_model(self, request, obj, form, change):
#         try:
#             # Попытка сохранения модели с вызовом проверки (clean)
#             obj.save()
#         except ValidationError as e:
#             # Если возникает ошибка валидации, отображаем её в форме
#             form.add_error(None, format_html('<span style="color: red;">{}</span>', str(e)))
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CertifiedCompany, Service, Observer
from .translation import *
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Service  # Импортируем модель
from .translation import *  # Импортируем файл translation

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('service',)  # Укажите поля для отображения


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'contact_number', 'address')
    search_fields = ('fullname', 'contact_number', 'address')

@admin.register(CertifiedCompany)
class CertifiedCompanyAdmin(TranslationAdmin):
    list_display = ('company_name', 'certificate_name', 'trademark', 'certificate_type', 'region', 'expiration_date')
    search_fields = ('company_name', 'certificate_name', 'trademark', 'region')
    list_filter = ('certificate_type', 'region', 'expiration_date')
    readonly_fields = ('qr_code', 'issue_date', 'expiration_date')
    fieldsets = (
        (None, {
            'fields': (
                'company_name',
                'certificate_name',
                'trademark',
                'service_type',
                'region',
                'observer',
                'company_address',
                'company_email',
                'registration_number',
                'certificate_photo',
                'company_photo'
            )
        }),
        ('Certificate Details', {
            'fields': (
                'issue_date',
                'expiration_date',
                'certificate_type',
                'qr_code'
            )
        }),
    )
    
    # Add functionality to display QR code image directly in the admin interface
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # During editing
            return readonly_fields + ('get_certificate_status_icon', 'get_certificate_status_text')
        return readonly_fields

    def get_certificate_status_icon(self, obj):
        return f'<img src="{obj.get_certificate_status_icon()}" alt="Certificate Status" />'
    
    get_certificate_status_icon.allow_tags = True
    get_certificate_status_icon.short_description = 'Certificate Status Icon'
    
    def get_certificate_status_text(self, obj):
        return obj.get_certificate_status_text()
    
    get_certificate_status_text.short_description = 'Certificate Status Text'

