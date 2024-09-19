from django.db import models
from Certification.models import CertifiedCompany


class ProductBarCode(models.Model):
    """
    Модель для представления штрих-кода продукта.
    """
    code = models.CharField(unique=True, max_length=30, verbose_name='Штрих код продукта')
    product_name = models.CharField(verbose_name='Название продукта')
    bar_type = models.CharField(max_length=6, choices=[('EAN_13', 'EAN_13'), ('UPC-A', 'UPC-A'), ('EAN-8', 'EAN-8'), ('UPC-E', 'UPC-E')], verbose_name='Тип кода продукта')
    product_status = models.CharField(max_length=42, choices=[('Проверенный', 'Проверенный'), ('Не проверенный', 'Не проверенный')], verbose_name='Статус продукта Проверенный/Не проверенный')
    company = models.ForeignKey(CertifiedCompany, on_delete=models.CASCADE, verbose_name='Компания')
    adal_center_icon = models.ImageField(upload_to='AdalCenterIcon/', verbose_name='Иконка сертифицированной компании Adal Center')
    product_image = models.ImageField(upload_to='BarCodeProductImages/', verbose_name='Изображение продукта')

    def __str__(self) -> str:
        return f'{self.product_name} - {self.bar_type}: {self.code} - статус: {self.product_status} - компания: {self.company.company_name}'
    
    class Meta:
        verbose_name = 'Штрих-код'
        verbose_name_plural = 'Штрих-коды'
