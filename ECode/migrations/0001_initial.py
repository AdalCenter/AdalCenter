# Generated by Django 5.0.8 on 2024-09-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ECode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=13, unique=True, verbose_name='Код продукта')),
                ('code_name', models.TextField(verbose_name='Название кода')),
                ('code_status', models.CharField(choices=[('Халяль (Разрешенные)', 'Халяль (Разрешенные)'), ('Машбух (Сомнительные)', 'Машбух (Сомнительные)'), ('Макрух (Нежелательные)', 'Макрух (Нежелательные)'), ('Харам (Запрещенные)', 'Харам (Запрещенные)')], max_length=42, verbose_name='Статус продукта')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Е-код',
                'verbose_name_plural': 'Е-коды',
            },
        ),
    ]
