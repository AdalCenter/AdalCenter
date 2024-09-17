from django.db import models
from Certification.models import CertifiedCompany


class ProductBarCode(models.Model):
    """
    Модель для представления штрих-кода продукта.
    """
    code = models.CharField(max_length=13, verbose_name='Код продукта')
    bar_type = models.CharField(
        max_length=6,
        choices=[('EAN_13', 'EAN_13'), ('UPC-A', 'UPC-A'), ('EAN-8', 'EAN-8'), ('UPC-E', 'UPC-E')],
        verbose_name='Тип кода продукта'
    )
    product_status = models.CharField(
        max_length=42,
        choices=[('Харам', 'Харам'), ('Халал', 'Халал'), ('Не проверено', 'Не проверено')],
        verbose_name='Статус продукта Адал/Харам/Не проверено'
    )
    company = models.ForeignKey(CertifiedCompany, on_delete=models.CASCADE, verbose_name='Компания')

    def __str__(self) -> str:
        return f'{self.bar_type}: {self.code} - статус: {self.product_status} - компания: {self.company.company_name}'
    
    class Meta:
        verbose_name = 'Штрих-код'
        verbose_name_plural = 'Штрих-коды'
