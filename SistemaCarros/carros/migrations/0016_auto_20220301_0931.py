# Generated by Django 3.2.10 on 2022-03-01 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0015_auto_20220228_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='fecha_registros',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='fotosCarro',
            field=models.ImageField(null=True, upload_to='fotosCarro/'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='garantia',
            field=models.ImageField(null=True, upload_to='garantia/'),
        ),
    ]
