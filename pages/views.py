from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from bookings.models import Booking
from django.utils.timezone import datetime
from cities.choices import city_choices, options, dance_choices



def index(request):

    today = datetime.today()
    bookings = Booking.objects.filter(is_advertised=True).filter(event_date__gte=today).order_by('event_date')


    paginator = Paginator(bookings, 15)
    page = request.GET.get('page')
    paged_bookings = paginator.get_page(page)


    context = {
        'bookings': paged_bookings,
        'city_choices': city_choices,
        'options': options,
        'dance_choices': dance_choices

    }
    return render(request, 'pages/index.html', context)



def job(request, booking_id):

    booking = get_object_or_404(Booking, pk=booking_id)

    context = {
        'booking': booking,
    }
    return render(request, 'pages/job_detail.html', context)


def job_search(request):
    today = datetime.today()
    queryset_list = Booking.objects.filter(is_advertised=True).filter(event_date__gte=today).order_by('event_date')

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



    context = {
        'bookings': queryset_list,
        'city_choices': city_choices,
        'options': options,
        'dance_choices': dance_choices

    }
    return render(request, 'pages/job_search.html', context)



