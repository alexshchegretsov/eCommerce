# Generated by Django 2.2.3 on 2019-07-09 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20190709_1952'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]