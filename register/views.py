from django.shortcuts import render

# Create your views here.

def show_home(request):
    return render(request,'register/addandshow.html')

def show_update(request):
    return render(request,'register/updateandshow.html')