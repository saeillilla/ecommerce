# Generated by Django 3.2.3 on 2021-05-26 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_product_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shipping_Adress',
        ),
    ]