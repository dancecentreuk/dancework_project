# Generated by Django 3.2.5 on 2021-09-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_alter_booking_booking_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='specific_song',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
