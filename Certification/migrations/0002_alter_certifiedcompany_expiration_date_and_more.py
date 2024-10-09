# Generated by Django 5.0.8 on 2024-10-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Certification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifiedcompany',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания сертификата'),
        ),
        migrations.AlterField(
            model_name='certifiedcompany',
            name='issue_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата получения сертификата'),
        ),
    ]
