# Generated by Django 5.2 on 2025-04-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("E11evenStore", "0008_transaccionpago"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="usuario",
            field=models.CharField(
                max_length=150, unique=True, verbose_name="Nombre Usuario"
            ),
        ),
    ]
