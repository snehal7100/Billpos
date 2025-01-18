# Generated by Django 3.2.25 on 2025-01-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PosMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('credit_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_term', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bill_date', models.DateField()),
            ],
            options={
                'db_table': 'tbl_pos_master',
            },
        ),
    ]
