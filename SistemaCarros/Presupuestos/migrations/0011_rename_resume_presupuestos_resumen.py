# Generated by Django 3.2.12 on 2022-03-29 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0010_presupuestos_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuestos',
            old_name='resume',
            new_name='resumen',
        ),
    ]
