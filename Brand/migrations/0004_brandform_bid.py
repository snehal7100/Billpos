# Generated by Django 5.1.4 on 2024-12-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0003_alter_brandform_bname'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandform',
            name='bid',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
