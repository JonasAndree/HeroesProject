from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
#request response cycle

def heroes_home(request):
    reg_form = RegisterForm(request.POST or None)
    login_form = LoginForm(request.POST or None)
    
    #email = request.POST['email']
    #password = request.POST['password']
    #user = authenticate(request, email=email, password=password)
    
    context = {
        "title":"Heroes",
        "reg_form": reg_form,
        "login_form":login_form
    }
    return render(request, "base.html", context)

def register_new(request):
    reg_form = RegisterForm(request.POST or None)
    return render(request, 'registration/register.html', {'reg_form': reg_form})