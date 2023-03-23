from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import portfolio

def home(request):
    resume = portfolio.objects.all()
    return render(request, 'home.html',{'resume':resume})
    
   
def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())
    return render(request, 'counter.html',{'amount': amount_words})

def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
        
            else:
                user = User.objects.create_user(email=email, username= username, password = password2)
                user.save();
                return redirect('login')
       else:
            messages.info(request,'password does not match') 
            return redirect('register')   
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate( username=username,password=password)

        if user is None:
            messages.info(request, 'invalid username or password')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('/')   
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
