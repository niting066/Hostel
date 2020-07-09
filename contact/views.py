from django.shortcuts import render, redirect
from contact.forms import *


# Create your views here.
# def contact(request):
# return render(request, 'contact/contact.html')


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('homepage')
    else:
        f = ContactForm()
    return render(request, 'contact/contact.html', {"cf": f})
