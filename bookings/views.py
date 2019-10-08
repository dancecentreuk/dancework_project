from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .models import Booking
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.timezone import datetime
from cities.choices import city_choices, options, dance_choices, deposit_options, booking_choices, venue_choices, balance_choices

# Create your views here.


def authorised_only(function):

    def _inner(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner


@login_required
@authorised_only
def bookings(request):

    today = datetime.today()
    bookings = Booking.objects.filter(event_date__gte=today).order_by('event_date')

    paginator = Paginator(bookings, 4)
    page = request.GET.get('page')
    paged_bookings = paginator.get_page(page)

    context = {

        'bookings': paged_bookings,
        'city_choices': city_choices,
        'dance_choices': dance_choices,
        'options': options


    }
    return render(request, 'bookings/bookings.html', context)



@login_required
def booking(request, booking_id):



    booking = get_object_or_404(Booking, pk=booking_id)
    get_dance_style = Booking.objects.filter(dance_style=booking_id)

    context = {
        'booking': booking,
        'poopstyle' : get_dance_style
    }
    return render(request, 'bookings/booking.html', context)


class BookingCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Booking
    fields = [ 'name', 'email', 'phone', 'initial_chat', 'event_date', 'book_before_date', 'event_length', 'booking_quantity', 'start_time', 'end_time', 'special_person',
               'dance_style', 'dance_style2', 'group_size', 'enquiry_date', 'city', 'venue_1', 'venue_2', 'venue_3', 'venue_4',
               'confirmed_venue', 'venue_booked', 'venue_paid', 'teacher', 'teacher_fee', 'teacher_confirmed', 'teacher_texted',
               'teacher_paid', 'cost', 'discount', 'workshop_booked', 'booking_sent', 'deposit_paid', 'agency', 'balance_paid',
               'problem', 'booking_notes',  'is_advertised',]

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Booking
    fields = ['name', 'email', 'phone', 'initial_chat', 'event_date', 'book_before_date', 'event_length', 'booking_quantity', 'start_time', 'end_time',
              'special_person',
              'dance_style', 'dance_style2', 'group_size', 'enquiry_date', 'city', 'venue_1', 'venue_2', 'venue_3', 'venue_4',
              'confirmed_venue', 'venue_booked', 'venue_paid', 'teacher', 'teacher_fee', 'teacher_confirmed',
              'teacher_texted',
              'teacher_paid', 'cost',  'discount', 'workshop_booked', 'booking_sent', 'deposit_paid', 'agency', 'balance_paid',
              'problem', 'booking_notes',  'is_advertised',]

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    success_url = '/bookings/'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


@login_required
@authorised_only
def search(request):
    today = datetime.today()
    queryset_list = Booking.objects.filter(event_date__gte=today).order_by('event_date')






    if 'booking_emailed' in request.GET:
        booking_emailed = request.GET['booking_emailed']
        if booking_emailed:
            queryset_list = queryset_list.filter(booking_sent__iexact=booking_emailed)




    # Dance style
    if 'style' in request.GET:
        style = request.GET['style']
        if style:
            queryset_list = queryset_list.filter(dance_style__dance_style__icontains=style)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__name__iexact=city)

    # Teacher Booked
    if 'teacher_booked' in request.GET:
        teacher_booked = request.GET['teacher_booked']
        if teacher_booked:
            queryset_list = queryset_list.filter(teacher_confirmed=teacher_booked)



    # Deposit Paid
    if 'deposit_paid' in request.GET:
        deposit_paid = request.GET['deposit_paid']
        if deposit_paid:
            queryset_list = queryset_list.filter(deposit_paid=deposit_paid)

    # Deposit Paid
    if 'balance_paid' in request.GET:
        balance_paid = request.GET['balance_paid']
        if balance_paid:
            queryset_list = queryset_list.filter(balance_paid=balance_paid)


    if 'venue_booked' in request.GET:
        venue_booked = request.GET['venue_booked']
        if venue_booked:
            queryset_list = queryset_list.filter(venue_booked = venue_booked)







    context = {
        'bookings': queryset_list,
        'city_choices': city_choices,
        'options': options,
        'dance_choices': dance_choices,
        'booking_emailed': booking_choices,
        'deposit_options': deposit_options,
        'venue_booked': venue_choices,
        'balance_paid': balance_choices


    }
    return render(request, 'bookings/search.html', context)


