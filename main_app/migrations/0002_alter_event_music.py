# Generated by Django 3.2.8 on 2021-10-30 06:36

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='music',
            field=models.FileField(blank=True, upload_to=main_app.models.get_audio_path),
        ),
    ]