# Generated by Django 4.2.16 on 2024-09-24 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padre_De_Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=14)),
                ('idPersona', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Persona.persona')),
            ],
        ),
    ]
