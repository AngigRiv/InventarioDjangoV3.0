# Generated by Django 4.2.6 on 2023-11-01 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_alter_inventario_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='responsable_linea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios_responsables', to='inventario.personal'),
        ),
    ]
