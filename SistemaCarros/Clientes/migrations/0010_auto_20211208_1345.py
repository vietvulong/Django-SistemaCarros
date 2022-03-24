# Generated by Django 3.2.9 on 2021-12-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0009_clientes_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='notas',
        ),
        migrations.AddField(
            model_name='clientes',
            name='ciudad',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='clientes',
            name='contacto_alternativo',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='clientes',
            name='contacto_alternativo2',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='clientes',
            name='contacto_alternativo3',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='clientes',
            name='corporacion',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='clientes',
            name='estado',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='clientes',
            name='fax',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='pais',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='clientes',
            name='social_media',
            field=models.CharField(default='0', max_length=80),
        ),
        migrations.AddField(
            model_name='clientes',
            name='social_media2',
            field=models.CharField(default='0', max_length=80),
        ),
        migrations.AddField(
            model_name='clientes',
            name='social_media3',
            field=models.CharField(default='0', max_length=80),
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefono2',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='website',
            field=models.URLField(default='0'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='zip',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipo',
            field=models.CharField(choices=[('Corporativo', 'Corporativo'), ('Persona', 'Persona')], default='Persona', max_length=200, null=True),
        ),
    ]
