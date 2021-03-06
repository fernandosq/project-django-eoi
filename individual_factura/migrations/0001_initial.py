# Generated by Django 3.1.3 on 2020-12-01 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.AutoField(primary_key=True, serialize=False)),
                ('anio', models.IntegerField()),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('cliente_nombre', models.CharField(max_length=30)),
                ('cliente_direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LineaDeFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('precio_unitario', models.IntegerField()),
                ('unidades', models.IntegerField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='individual_factura.factura')),
            ],
        ),
    ]
