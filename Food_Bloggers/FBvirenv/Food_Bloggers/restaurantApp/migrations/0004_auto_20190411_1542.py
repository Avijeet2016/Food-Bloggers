# Generated by Django 2.1 on 2019-04-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0003_auto_20190410_2351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['id']},
        ),
    ]