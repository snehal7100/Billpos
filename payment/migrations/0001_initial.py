# Generated by Django 3.2.25 on 2025-01-10 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(default='1', max_length=255)),
                ('pname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_payment',
            },
        ),
    ]
