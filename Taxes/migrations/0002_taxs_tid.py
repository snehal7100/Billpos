# Generated by Django 5.1 on 2024-12-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taxes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxs',
            name='tid',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
