# Generated by Django 5.0.8 on 2024-08-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='AboutUs_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordinate_title', models.CharField(max_length=255)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('url_title', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='FAQ_Icon/')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Locate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36)),
                ('text', models.TextField()),
                ('icon', models.ImageField(upload_to='OurAchievement_icon/')),
            ],
        ),
        migrations.CreateModel(
            name='OurAchievementCertificateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Certificates_image/')),
            ],
        ),
        migrations.CreateModel(
            name='OurGoalsAndObjectives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=34)),
                ('last_name', models.CharField(blank=True, max_length=34, null=True)),
                ('image', models.ImageField(upload_to='TeamPeople_Icon/')),
                ('speciality', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='PartnerLogo/')),
                ('url', models.URLField()),
            ],
        ),
    ]
