from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm,RegisterForm,GuestForm
from .models import GuestEmail
from django.utils.http import is_safe_url
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def guest_register_view(request):
    form = GuestForm(request.POST or None)
    
    context = {
        'form':form
        
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        print(email)
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)  
        
        else:
                # Return an 'invalid login' error message.
            return redirect('cart:checkout')
    return redirect('/register/')  

User = get_user_model()
def register_page(request):
    if request.method == 'POST':
        #Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check If Passwords Match
        if password == password2:
         #Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request,'The Username has been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'The email has been used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,
                    first_name=first_name,last_name=last_name)
                    #Login After Register
                    # auth.login(request,user)
                    user.save()
                    messages.success(request,'You are now Registered and can Login')
                    return redirect('login')
        else:  
            messages.error(request,'Passwords Do Not Match') 
            return redirect('register') 
       
    else:
        return render (request,'accounts/register.html')  


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials') 
            return redirect('login')   
    else:
        return render (request,'accounts/login.html')  

def dashboard_page(request):
    return render(request,'accounts/dashboard.html')
def logout_page(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('home')