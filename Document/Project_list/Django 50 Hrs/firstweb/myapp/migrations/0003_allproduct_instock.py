# Generated by Django 3.0 on 2021-07-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_allproduct_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='instock',
            field=models.BooleanField(default=True),
        ),
    ]