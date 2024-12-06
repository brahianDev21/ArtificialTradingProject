from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Username or password is incorrect.")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

@login_required 
def index(request):
    return render(request, 'index.html')
