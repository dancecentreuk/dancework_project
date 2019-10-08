from django.contrib import admin


from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'special_person', 'dance_style', 'city', 'deposit_paid', 'venue_booked', 'enquiry_date')
    list_display_links = ('name',)
    list_filter = ('city', 'dance_style', 'enquiry_date')
    search_fields = ('name',  'special_person', 'dance_style__dance_style',  'booking_notes',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Booking, BookingAdmin)
