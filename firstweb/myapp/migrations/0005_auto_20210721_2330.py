# Generated by Django 3.0 on 2021-07-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_allproduct_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='allproduct',
            name='unit',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
