# Generated by Django 3.2.10 on 2022-02-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0010_carro_motor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='motor',
            field=models.CharField(max_length=255),
        ),
    ]
