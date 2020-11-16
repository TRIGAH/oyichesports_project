from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.

def about(request):
    return render(request,'pages/about_us.html')
def contact(request):
    return render(request,'pages/contact.html')
def checkout(request):
    return render(request,'pages/checkout.html')
def gallery(request):
    return render(request,'pages/gallery_masonry.html')
def news(request):
    return render(request,'pages/news.html')
def team(request):

    return render (request,'accounts/dashboard.html')  

def add_player(request):
    return render(request,'pages/add_player.html')
def results(request):
    return render(request,'pages/results.html')
def page_404(request):
    return render(request,'pages/404.html')
