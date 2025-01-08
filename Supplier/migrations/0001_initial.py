# Generated by Django 3.2.25 on 2024-12-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('gst_no', models.CharField(blank=True, max_length=15, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('group_type', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_address', models.TextField()),
                ('shipping_address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('credit_limit', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('credit_period', models.PositiveIntegerField(default=0)),
                ('supplier_barcode', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_supplier',
            },
        ),
    ]