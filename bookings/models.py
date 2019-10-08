from django.db import models
from datetime import datetime
from cities.models import City, Studio, Venue
from styles.models import Style
from teachers.models import Teacher
from django.urls import reverse
from cities.choices import length_choices
from django.template.defaultfilters import slugify


# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    initial_chat = models.BooleanField(default=False)
    event_date = models.DateField()
    event_length = models.CharField(
        choices = length_choices,
        max_length=5,
        default=None
    )
    booking_quantity = models.DecimalField(max_digits=2, decimal_places=1)
    book_before_date = models.DateField()
    start_time= models.CharField(max_length=10, blank=True)
    end_time = models.CharField(max_length=10, blank=True)
    special_person = models.CharField(max_length=80, blank=True)
    dance_style = models.ForeignKey(Style, on_delete=models.DO_NOTHING,)
    dance_style2 = models.ForeignKey(Style, related_name='second_dance', on_delete=models.DO_NOTHING, blank=True, null=True)
    group_size = models.IntegerField(blank=True, null=True)
    enquiry_date = models.DateTimeField(default=datetime.now, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    venue_1 = models.ForeignKey(Venue, related_name='venue_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    venue_2 = models.ForeignKey(Venue, related_name='venue_2', on_delete=models.DO_NOTHING, blank=True, null=True)
    venue_3 = models.ForeignKey(Venue, related_name='venue_3', on_delete=models.DO_NOTHING, blank=True, null=True)
    venue_4 = models.ForeignKey(Venue, related_name='venue_4', on_delete=models.DO_NOTHING, blank=True, null=True)
    confirmed_venue = models.ForeignKey(Venue, related_name='confirmed_venue', on_delete=models.DO_NOTHING, blank=True, null=True)
    venue_booked = models.BooleanField(default=False)
    venue_paid = models.BooleanField(default=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=True, null=True)
    teacher_fee = models.IntegerField(blank=True, null=True)
    teacher_confirmed = models.BooleanField(default=False)
    teacher_texted = models.BooleanField(default=False)
    teacher_paid = models.BooleanField(default=False)
    cost = models.IntegerField(blank=True)
    discount = models.IntegerField(blank=True, default=0)
    venue_cost = models.IntegerField(blank=True, null=True)
    is_advertised = models.BooleanField(default=False)
    workshop_booked = models.BooleanField(default=False)
    booking_sent = models.BooleanField(default=False)
    deposit_paid = models.BooleanField(default=False)
    agency = models.BooleanField(default=False)
    balance_paid = models.BooleanField(default=False)
    problem = models.BooleanField(default=False)
    booking_notes = models.TextField(blank=True)


    def __str__(self):
        return self.name




    def studio_cost(self):
        if self.confirmed_venue:
            return self.confirmed_venue.cost * self.booking_quantity
        else:
            return 0

    def workshop_cost(self):
        if self.booking_quantity == 1:
            return self.cost - 30
        else:
            if self.booking_quantity == 1.5:
                return self.cost






    def total_cost(self):
        return self.studio_cost() + self.workshop_cost() - self.discount

    def balance(self):
        return self.total_cost() - 50

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Booking, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bookings:booking', kwargs={'booking_id': self.pk})
