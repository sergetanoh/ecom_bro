# Generated by Django 5.0.2 on 2024-03-24 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0007_alter_commande_numero_maillot"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="photo3",
        ),
        migrations.RemoveField(
            model_name="commande",
            name="nom_maillot",
        ),
        migrations.RemoveField(
            model_name="commande",
            name="numero_maillot",
        ),
    ]
