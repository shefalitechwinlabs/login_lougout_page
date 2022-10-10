from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            request.session['username'] = username
            return redirect('home')
        else:
            context = {'error':'Username or password is incorrect!'}
            return render (request,'login.html', context)
        
    if "username" in request.session:
        return redirect('home/')
    else:
        return render(request,'login.html')
  
  

def logout(request):
    auth.logout(request)
    username = request.session.get('username')
    del username
    return render (request, 'logout.html')

