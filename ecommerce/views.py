from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate , login, logout
from .forms import ProductForm
from django.views import  View

# Create your views here.
# def store_page(request):
    
#     products = Product.objects.all()
#     return render(request, 'ecommerce/store.html', {
#         'products': products
# 



class StorePageView(View):
    template_name = 'ecommerce/store.html'
    
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        return render(request,
                      self.template_name,
                      {'products': products})
    
    
    
    
# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
        
        
#         user = authenticate(request,username=username,password=password)
        
#         if user is not None:
#             login(request,user)
#             return redirect('home_page')
            

#     return render(request, 'ecommerce/login.html')


class LoginPageView(View):
    template_name = 'ecommerce/login.html'
    
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{})
    
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home_page')
        
        return render(request,self.template_name,{})
    
# def logout_page(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login_page')
        
#     return render(request,'ecommerce/logout.html',{})


class LogoutPage(View):
     template_name = 'ecommerce/logout.html'
     def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

     def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login_page')


class NewProductView(View):
    template_name = 'ecommerce/new_product.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)

        return redirect('home_page')
        return render(request, self.template_name, {'form': form})
    
        
# def new_product(reuest):
#     form = ProductForm()
#     return render(reuest,'ecommerce/new_product.html',{
#         'form' : form
#     })
   