# Generated by Django 3.0.6 on 2020-07-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0008_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]