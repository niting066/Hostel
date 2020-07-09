from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def admin_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signupAdmin.html', {"form": form})


def adminpanel(request):
    return render(request, 'admintemp/AdminHomepage.html',)


def homepage(request):
    return render(request, 'index.html')


def admin(request):
    return render(request, 'registration/admin_homepage.html')
