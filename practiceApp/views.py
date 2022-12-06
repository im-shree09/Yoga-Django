from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Contact

# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        site=request.POST.get('site')
        desc=request.POST.get('desc')

        contact= Contact(name=name,email=email,phone=phone,site=site,desc=desc)
        contact.save()
        print('successfull!')
        
    return render(request,'index.html')

def home(request):
    comments= Contact.objects.all()
    context={
        'comments':comments
    }
    print(context)
    return render(request,'home.html',context)

def yoga1(request):
    comments= Contact.objects.all()
    context={
        'comments':comments
    }
    print(context)

    return render(request,'yoga1.html',context)

def yoga2(request):
    comments= Contact.objects.all()
    context={
        'comments':comments
    }
    print(context)

    return render(request,'yoga2.html',context) 

def yoga3(request):
    comments= Contact.objects.all()
    context={
        'comments':comments
    }
    print(context)

    return render(request,'yoga3.html',context)

