# Generated by Django 3.2.5 on 2021-09-06 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0005_alter_studio_photo_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='photo_promo',
            field=models.ImageField(blank=True, upload_to='photos/studio/%Y/%m/%d/'),
        ),
    ]
