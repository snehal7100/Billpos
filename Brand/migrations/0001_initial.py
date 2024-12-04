# Generated by Django 5.1.3 on 2024-12-04 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=255)),
                ('img', models.FileField(max_length=255, null=True, upload_to='pics/')),
            ],
            options={
                'db_table': 'tbl_Brand',
            },
        ),
    ]
