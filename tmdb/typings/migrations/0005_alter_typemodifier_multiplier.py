# Generated by Django 4.2.5 on 2024-09-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typings', '0004_typemodifier_delete_typeadvantage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typemodifier',
            name='multiplier',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
