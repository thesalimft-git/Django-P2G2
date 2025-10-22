from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate , login, logout
from .forms import ProductForm
from django.views import  View
from .forms import ContactUsForm
from .models import ContactUs

# Create your views here.
class ContactUsPage(View):
    template_name = 'ecommerce/contact_us.html'

    def get(self, request, *args, **kwargs):
        form = ContactUsForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_filled = ContactUsForm(data=request.POST)
        if form_filled.is_valid():
            form_filled.save()
        
        
        return render(request, self.template_name, {})



class StorePageView(View):
    template_name = 'ecommerce/store.html'  
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        return render(request,
                      self.template_name,
                      {'products': products})

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
    
        
# section function base     
# def new_product(reuest):
#     form = ProductForm()
#     return render(reuest,'ecommerce/new_product.html',{
#         'form' : form
#     })
   
   
# def store_page(request):
    
#     products = Product.objects.all()
#     return render(request, 'ecommerce/store.html', {
#         'products': products
# 

    
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

    
# def logout_page(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login_page')
        
#     return render(request,'ecommerce/logout.html',{})
