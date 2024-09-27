from django.db import models
from django.utils.translation import gettext_lazy as _

class ECode(models.Model):
    HALAL = _('Халяль (Разрешенные)')
    MASHBUH = _('Машбух (Сомнительные)')
    MAKRUH = _('Макрух (Нежелательные)')
    HARAM = _('Харам (Запрещенные)')

    CODE_STATUS_CHOICES = [
        (HALAL, _('Халяль (Разрешенные)')),
        (MASHBUH, _('Машбух (Сомнительные)')),
        (MAKRUH, _('Макрух (Нежелательные)')),
        (HARAM, _('Харам (Запрещенные)'))
    ]

    code = models.CharField(unique=True, max_length=13, verbose_name=_('Код продукта'))
    code_name = models.TextField(verbose_name=_('Название кода'))
    code_status = models.CharField(max_length=42, choices=CODE_STATUS_CHOICES, verbose_name=_('Статус продукта'))
    description = models.TextField(verbose_name=_('Описание'))

    def __str__(self) -> str:
        return f'E код: {self.code} - Статус кода: {self.code_status}'

    class Meta:
        verbose_name = _('Е-код')
        verbose_name_plural = _('Е-коды')
