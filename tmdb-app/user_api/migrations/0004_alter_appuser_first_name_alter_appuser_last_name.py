# Generated by Django 4.2.5 on 2023-11-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_appuser_first_name_appuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]