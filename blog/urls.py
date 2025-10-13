from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('card/', views.card_page, name='card_page'),
    path('about-us/', views.about_us_page, name='about_us_page'),
    path('contact-us/', views.contact_us_page, name='contact_us_page'),
    
]
