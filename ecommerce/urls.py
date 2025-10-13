from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store_page, name='store_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('new-product/', views.new_product, name='new_product'),
]