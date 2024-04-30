from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('index/', views.index, name='index'),
    path('index/login', views.login, name='login'),


    path('distance', views.distance, name='distance'),

    path('map/', views.map, name='map'),
    path('weather/', views.weather, name='weather'),

    path('contact/', views.contact, name='contact'),
    path('contact/contact_data', views.contact_data, name='contact_data'),

    path('registration/', views.registration, name='registration'),
    path('registration/registration_data', views.registration_data, name='registration_data'),

]
