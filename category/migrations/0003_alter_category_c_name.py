from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_c_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='c_name',
            field=models.CharField(max_length=255),
        ),
    ]
