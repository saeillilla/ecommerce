# Generated by Django 3.2.3 on 2021-05-26 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210526_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing_adress',
            name='Apartment',
        ),
        migrations.AddField(
            model_name='billing_adress',
            name='Adress',
            field=models.TextField(blank=True),
        ),
    ]
