# Generated by Django 3.2.8 on 2021-10-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_event_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]