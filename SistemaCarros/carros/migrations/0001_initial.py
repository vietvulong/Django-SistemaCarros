# Generated by Django 3.2.7 on 2021-10-06 02:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField(default=datetime.timezone)),
                ('marca', models.CharField(max_length=255)),
                ('serie', models.CharField(max_length=255)),
                ('motor', models.CharField(max_length=255)),
                ('sistema_direccion', models.CharField(max_length=255)),
                ('sistema_combustión', models.CharField(max_length=255)),
                ('transmision', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('placas', models.CharField(max_length=255)),
                ('tipo_gasolina', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('año', models.IntegerField()),
            ],
        ),
    ]
