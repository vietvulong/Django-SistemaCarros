# Generated by Django 3.2.7 on 2021-10-25 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0002_alter_carro_fecha_ingreso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='fecha_ingreso',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='carro',
            old_name='marca',
            new_name='vin',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='serie',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='sistema_combustión',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='sistema_direccion',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='tipo_gasolina',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='transmision',
        ),
    ]
