from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.StorePageView.as_view(), name='store_page'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('new-product/', views.new_product, name='new_product'),
]