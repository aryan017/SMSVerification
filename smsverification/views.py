from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

@login_required
def home_view(request):
    return render(request,'main.html',{})

def auth_view(request):
   form=AuthenticationForm()
   if request.method=="POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
