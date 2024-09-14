from django.db import models
from Certification.models import *


class ProductBarCode(models.Model):
    code = models.CharField(max_length=13)
    bar_type = models.CharField(max_length=6, choices=[('EAN_13', 'EAN_13'), ('UPC-A', 'UPC-A'), ('EAN-8', 'EAN-8'), ('UPC-E', 'UPC-E')])
    product_status = models.CharField(max_length=42)
    company = models.ForeignKey(CertifiedCompany, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.bar_type}: {self.code} - status: {self.product_status} - company ID: {self.company.company_name}'
