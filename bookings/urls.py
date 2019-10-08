from django.urls import path
from .views import bookings, booking, BookingCreateView, BookingUpdateView, search, BookingDeleteView


app_name = 'bookings'

urlpatterns = [
    path('', bookings, name='bookings'),
    path('booking/<int:booking_id>/', booking, name='booking'),
    path('create', BookingCreateView.as_view(), name='booking-create'),
    path('booking/update/<int:pk>/', BookingUpdateView.as_view(), name='booking-update'),
    path('booking/delete/<int:pk>/', BookingDeleteView.as_view(), name='booking-delete'),
    path('search', search, name='search'),


]