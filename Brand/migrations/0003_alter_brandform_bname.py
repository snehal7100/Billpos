# Generated by Django 5.1.3 on 2024-12-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0002_alter_brandform_bname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandform',
            name='bname',
            field=models.CharField(max_length=255),
        ),
    ]
