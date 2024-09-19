from django.db import models


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

    code = models.CharField(unique=True, max_length=13, verbose_name='Код продукта')
    code_name = models.CharField(max_length=50, verbose_name='Название кода')
    code_status = models.CharField(max_length=42, choices=CODE_STATUS_CHOICES, verbose_name='Статус продукта')
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return f'E код: {self.code} - Статус кода: {self.code_status}'

    class Meta:
        verbose_name = 'Е-код'
        verbose_name_plural = 'Е-коды'
