# Generated by Django 5.0.8 on 2024-10-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Certification', '0002_alter_certifiedcompany_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifiedcompany',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и времени окончания сертификата'),
        ),
        migrations.AlterField(
            model_name='certifiedcompany',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и времени получения сертификата'),
        ),
    ]
