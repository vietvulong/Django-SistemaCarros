# Generated by Django 3.2.10 on 2022-05-23 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0008_alter_presupuestos_status'),
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoices',
            old_name='fecha_registro',
            new_name='date_resigter',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='cantidadInvoice',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='cuentaInvoice',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='fechaInvoice',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='invoiceId',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='statusInvoice',
        ),
        migrations.AddField(
            model_name='invoices',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='invoices',
            name='estimate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Presupuestos.presupuestos'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
