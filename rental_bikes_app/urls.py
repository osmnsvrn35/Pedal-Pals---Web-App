from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('bicycle_rental/', views.main_page, name='main_page'),
    path('',RedirectView.as_view(url='/bicycle_rental',permanent = True)),

    path('bicycle_rental/login', views.login_view, name='login'),
    path('bicycle_rental/registration', views.registration, name='registration'),
    
    path('bicycle_rental/forgot_password', views.forgot_password, name='forgot_password'),
    path('bicycle_rental/e_bikes', views.e_bikes, name='e_bikes'),
    path('logout/', views.logout_view, name='logout'),
    path('bicycle_rental/mountain_bikes', views.mountain_bikes, name='mountain_bikes'),
    path('bicycle_rental/road_bikes', views.road_bikes, name='road_bikes'),
    path('bicycle_rental/city_bikes', views.city_bikes, name='city_bikes'),
    path('bicycle_rental/city_bikes/reservation', views.rental_view, name='reservation'),
    path('bicycle_rental/road_bikes/reservation', views.rental_view, name='reservation'),
    path('bicycle_rental/mountain_bikes/reservation/<int:bike_id>', views.rental_view, name='reservation'),
    path('bicycle_rental/e_bikes/reservation', views.rental_view, name='reservation'),
    path('bicycle_rental/report_damage',views.report_damage,name='report_damage'),
    path('bicycle_rental/bike_history',views.bike_history,name='bike_history'),
]       

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
