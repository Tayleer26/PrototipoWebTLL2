# Generated by Django 4.2.16 on 2024-09-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sector', models.CharField(max_length=50)),
                ('Zona', models.CharField(max_length=50)),
            ],
        ),
    ]
