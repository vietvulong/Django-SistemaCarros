# Generated by Django 3.2.10 on 2022-06-17 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0002_alter_presupuestos_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestos',
            name='total_manaobra',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='presupuestos',
            name='total_parte',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
