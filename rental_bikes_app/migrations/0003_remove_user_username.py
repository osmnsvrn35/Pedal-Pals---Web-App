# Generated by Django 4.1.3 on 2023-01-22 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental_bikes_app', '0002_remove_bike_price_per_hour_bike_price_per_day_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
