# Generated by Django 3.2.5 on 2021-07-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_auto_20210707_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='photo_promo',
            field=models.ImageField(blank=True, upload_to='photos/studio/%Y/%m/%d/'),
        ),
    ]