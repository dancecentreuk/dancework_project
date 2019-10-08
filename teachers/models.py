from django.db import models
from cities.choices import city_choices
from django.urls import reverse


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='static/img/default-teachers-pic.jpg')
    city = models.CharField(
        choices=city_choices,
        max_length=100,
        default=None
    )
    address = models.CharField(max_length=300, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    speciality = models.TextField()
    fee = models.IntegerField()
    notes = models.TextField(blank=True)
    dance_school_attended = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )

    def get_absolute_url(self):
        return reverse('teachers:teacher-detail', kwargs={'teacher_id': self.pk})
