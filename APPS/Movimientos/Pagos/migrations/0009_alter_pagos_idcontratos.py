# Generated by Django 4.2.16 on 2024-09-25 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contrato', '0001_initial'),
        ('Pagos', '0008_pagos_idcontratos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='idContratos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Contrato.contratos'),
        ),
    ]
