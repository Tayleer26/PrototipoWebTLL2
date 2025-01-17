# Generated by Django 4.2.16 on 2024-09-24 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rutas', '0001_initial'),
        ('Trabajadores', '0001_initial'),
        ('Vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalles_De_Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=300)),
                ('Turno', models.CharField(max_length=20)),
                ('Fecha', models.DateTimeField()),
                ('idRutas', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Rutas.rutas')),
                ('idTrabajadores', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Trabajadores.trabajadores')),
                ('idVehiculos', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Vehiculo.vehiculo')),
            ],
        ),
    ]
