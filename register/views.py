from re import U
from django.shortcuts import render
from .forms import UserRegistration
from .models import User
# Create your views here.

def show_home(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            # 1st method to directly save using save method
            # fm.save()
            # or
            # 2nd method is we can extract all the fields manually and then save it using models...
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name,email=email,password=password)
            reg.save()
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    return render(request,'register/addandshow.html',{'form':fm})

def show_update(request):
    return render(request,'register/updateandshow.html')