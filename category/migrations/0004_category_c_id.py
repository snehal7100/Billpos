# Generated by Django 5.1 on 2024-12-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_c_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='c_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
