from django.db import models
from django.urls import reverse
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO
from django.core.files import File

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the City name')

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Studio(models.Model):
    studio_name = models.CharField(max_length=200, help_text='Enter Studio or website name')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    studio_website = models.URLField(max_length=200, blank=True)
    studio_email = models.CharField(max_length=200, help_text='Enter Studio contact')
    studio_mobile = models.CharField(max_length=15, help_text='Enter contact number')
    studio_contact = models.CharField(max_length=200, default='James Cooke')

    def __str__(self):
        return self.studio_name


class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300,  blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    postcode = models.CharField(max_length=10, blank=True)
    venue_phone = models.CharField(max_length=20,  blank=True)
    venue_coordinator = models.CharField(max_length=200, blank=True)
    venue_email = models.CharField(max_length=300,  blank=True)
    venue_website = models.URLField(max_length=200,  blank=True)
    capacity = models.IntegerField(blank=True)
    cost = models.IntegerField( blank=True)
    venue_cost = models.IntegerField(blank=True,)
    no_studios = models.IntegerField(default=1)
    photo_main = models.ImageField(upload_to='photos/venue/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/venue/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/venue/%Y/%m/%d/', blank=True)
    notes = models.TextField(blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        memfile = BytesIO()


        if self.photo_main:
            img = Image.open(self.photo_main)
            if img.height > 250 or img.width > 250:
                output_size = (250, 250)
                img.thumbnail(output_size, Image.ANTIALIAS)
                img.save(memfile, 'PNG', quality=95 )
                default_storage.save(self.photo_main.name, memfile)
                memfile.close()
                img.thumbnail(output_size)
                img.save(self.photo_main.path)
                img.close()


        if self.photo_1:
            img2 = Image.open(self.photo_1)
            if img2.height > 250 or img.width > 250:
                output_size = (250, 250)
                img2.thumbnail(output_size, Image.ANTIALIAS)
                img2.save(memfile, 'PNG', quality=95)
                default_storage.save(self.photo_1.name, memfile)
                memfile.close()
                img2.thumbnail(output_size)
                img2.save(self.photo_1.path)
                img2.close()




    def photo_main_url (self):
        if self.photo_main:
            return self.photo_main.url

    @property
    def photo_1_url(self):
        if self.photo_1 and hasattr(self.photo_1, 'url'):
            return self.photo_1.url

    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return reverse('cities:venue-detail', kwargs={'venue_id': self.pk})












