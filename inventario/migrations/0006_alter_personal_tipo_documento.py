# Generated by Django 4.2.6 on 2023-10-31 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_rename_empresa_id_articulo_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='tipo_documento',
            field=models.IntegerField(choices=[(1, 'DNI'), (2, 'Carnet de Extranjería'), (3, 'Otro')]),
        ),
    ]