# Generated by Django 4.1.3 on 2023-06-23 23:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='numero_client',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')]),
        ),
    ]