
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts.views import register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('staff/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('', include('pages.urls')),
    path('bookings/', include('bookings.urls')),
    path('teachers/', include('teachers.urls')),
    path('venues/', include('cities.urls')),
    path('contact/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


