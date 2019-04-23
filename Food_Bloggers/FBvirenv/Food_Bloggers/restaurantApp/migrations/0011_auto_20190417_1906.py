# Generated by Django 2.1 on 2019-04-17 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0010_auto_20190417_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurantApp.Restaurant'),
        ),
    ]
