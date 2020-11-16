from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model

def home(request):
    # print( request.session.get('first_name'))
    context = {
       'hello':'Hello We Are Coming',
       'premium':'You Are Welcome'
    }
    
    return render(request,'pages/home.html',context)

def contact_page(request):
    contact_form=ContactForm(request.POST or None)
    context={
        'cont':contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'pages/contact.html',context)

       
