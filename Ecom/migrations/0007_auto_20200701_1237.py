# Generated by Django 3.0.6 on 2020-07-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0006_item_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]