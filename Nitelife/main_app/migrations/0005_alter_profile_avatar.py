# Generated by Django 3.2.8 on 2021-10-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211025_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='', upload_to='p_image'),
        ),
    ]
