# Generated by Django 3.0 on 2021-07-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_allproduct_instock'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]