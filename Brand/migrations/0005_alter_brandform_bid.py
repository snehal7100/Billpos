
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0004_brandform_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandform',
            name='bid',
            field=models.CharField(default='1', max_length=255),
        ),
    ]
