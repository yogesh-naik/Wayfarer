# Generated by Django 3.2.8 on 2021-10-14 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211014_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='efk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='main_app.event'),
        ),
    ]