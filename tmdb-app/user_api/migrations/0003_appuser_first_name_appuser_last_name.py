# Generated by Django 4.2.5 on 2023-11-06 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_alter_appuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]