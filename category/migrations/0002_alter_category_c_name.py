

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='c_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
