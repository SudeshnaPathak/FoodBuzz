# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate , logout
from .forms import CustomUserCreationForm, AddressForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def SignupPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# accounts/views.py

def LoginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def change_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
              # Replace 'view' with the name of the view you want to redirect to after saving
    else:
        form = AddressForm(instance=request.user.userprofile)
    return render(request, 'address.html', {'form': form})
def logoutPage(request):
    logout(request)
    return redirect('login')

def conclusion(request):
    return render(request, 'thankyou.html')