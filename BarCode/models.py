from django.db import models
from django.utils.translation import gettext_lazy as _
from Certification.models import CertifiedCompany


class ProductBarCode(models.Model):
    """
    Модель для представления штрих-кода продукта.
    """
    code = models.CharField(unique=True, max_length=14, verbose_name=_('Штрих код продукта'))
    product_name = models.TextField(verbose_name=_('Название продукта'))
    
    BAR_TYPE_CHOICES = [
        ('EAN_13', _('EAN_13')),
        ('UPC-A', _('UPC-A')),
        ('EAN-8', _('EAN-8')),
        ('UPC-E', _('UPC-E')),
    ]
    bar_type = models.CharField(max_length=6, choices=BAR_TYPE_CHOICES, verbose_name=_('Тип кода продукта'))
    
    PRODUCT_STATUS_CHOICES = [
        ('Проверенный', _('Проверенный')),
        ('Не проверенный', _('Не проверенный')),
    ]
    product_status = models.CharField(max_length=42, choices=PRODUCT_STATUS_CHOICES, verbose_name=_('Статус продукта Проверенный/Не проверенный'))
    company = models.ForeignKey(CertifiedCompany, on_delete=models.CASCADE, verbose_name=_('Компания'))
    adal_center_icon = models.ImageField(upload_to='AdalCenterIcon/', verbose_name=_('Иконка сертифицированной компании Adal Center'))
    product_image = models.ImageField(upload_to='BarCodeProductImages/', verbose_name=_('Изображение продукта'))

    def __str__(self) -> str:
        return f'{self.product_name} - {self.bar_type}: {self.code} - статус: {self.product_status} - компания: {self.company.company_name}'
    
    class Meta:
        verbose_name = _('Штрих-код')
        verbose_name_plural = _('Штрих-коды')
