from django.db import models
from Certification.models import CertifiedCompany


class TypeOfOrigin(models.Model):
    type_of_origin = models.CharField(max_length=35, verbose_name='Тип происхождения', unique=True)

    def __str__(self) -> str:
        return self.type_of_origin
    
    class Meta:
        verbose_name = 'Тип происхождения'
        verbose_name_plural = 'Типы происхождения'

class CodeType(models.Model):
    code_type = models.CharField(max_length=35, verbose_name='Тип кода', unique=True)

    def __str__(self) -> str:
        return self.code_type
    
    class Meta:
        verbose_name = 'Тип кода'
        verbose_name_plural = 'Типы кодов'

class ECode(models.Model):
    HALAL = 'Халяль (Разрешенные)'
    MASHBUH = 'Машбух (Сомнительные)'
    MAKRUH = 'Макрух (Нежелательные)'
    HARAM = 'Харам (Запрещенные)'

    CODE_STATUS_CHOICES = [
        (HALAL, 'Халяль (Разрешенные)'),
        (MASHBUH, 'Машбух (Сомнительные)'),
        (MAKRUH, 'Макрух (Нежелательные)'),
        (HARAM, 'Харам (Запрещенные)')
    ]

    code = models.CharField(max_length=13, verbose_name='Код продукта', unique=True)
    code_name = models.CharField(max_length=30, verbose_name='Название кода')
    code_type = models.ForeignKey(CodeType, verbose_name='Тип кода')
    type_of_origin = models.ForeignKey(TypeOfOrigin, verbose_name='Тип происхождения')
    mini_description = models.TextField(verbose_name='Мини описание для вывода в список кодов')
    code_status = models.CharField(max_length=42, choices=CODE_STATUS_CHOICES, verbose_name='Статус продукта')
    description = models.TextField(verbose_name='Описание')
    usage = models.TextField(verbose_name='Использование')

    def __str__(self) -> str:
        return f'E код: {self.code} - Статус кода: {self.code_status}'

    class Meta:
        verbose_name = 'Е-код'
        verbose_name_plural = 'Е-коды'
