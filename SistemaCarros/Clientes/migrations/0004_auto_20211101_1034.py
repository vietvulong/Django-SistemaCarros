# Generated by Django 3.2.7 on 2021-11-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_clientes_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
