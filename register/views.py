from re import U
from django.http import HttpResponseRedirect
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
    get_all = User.objects.all()

    return render(request,'register/addandshow.html',{'form':fm,'show':get_all})

def show_update(request):
    return render(request,'register/updateandshow.html')

def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home/add/')