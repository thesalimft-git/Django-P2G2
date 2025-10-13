from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate , login, logout
from .forms import ProductForm

# Create your views here.
def store_page(request):
    
    products = Product.objects.all()
    return render(request, 'ecommerce/store.html', {
        'products': products
    })
    
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home_page')
            

    return render(request, 'ecommerce/login.html')
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_page')
        
    return render(request,'ecommerce/logout.html',{})
        
def new_product(reuest):
    form = ProductForm()
    return render(reuest,'ecommerce/new_product.html',{
        'form' : form
    })
   