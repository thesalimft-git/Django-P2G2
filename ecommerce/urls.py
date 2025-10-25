from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.StorePageView.as_view(), name='store_page'),
    path('products/<int:id>', views.ProductDetailPageView.as_view(), name='product_detail_page'),
    
    
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('logout/', views.LogoutPage.as_view(), name='logout_page'),
    path('new-product/', views.NewProductView.as_view(), name='new_product'),
    path('contact-us/', views.ContactUsPage.as_view(), name='contact_us_page'),
]