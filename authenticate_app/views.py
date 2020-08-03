from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.
def loginPage(request):
    return render(request,"login.html")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"user created successfully")
            return redirect('login')
        else:
            messages.error(request,"there was an error")
            
    return render(request,"signup.html",{'form':form})