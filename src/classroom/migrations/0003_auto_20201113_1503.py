# Generated by Django 3.1.3 on 2020-11-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20201112_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
