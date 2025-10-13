from django.shortcuts import render
from django.http import HttpResponse



def home_page(request):
    return render(request, 'blog/store.html', {})

def card_page(request):
    return render(request, 'blog/card.html', {})

def about_us_page(request):
    return render(request, 'blog/about_us.html', {})

def contact_us_page(request):
    return render(request, 'blog/contact_us.html', {})