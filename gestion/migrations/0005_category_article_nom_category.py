# Generated by Django 4.2.3 on 2023-07-15 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_alter_commande_numero_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='nom_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.category'),
        ),
    ]