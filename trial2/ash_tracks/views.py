from django.shortcuts import render
from .models import Contact, Register


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(email=email, subject=subject, message=message)
        c.save()

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        discription = request.POST.get('discription')

        c = Register(email=email, fullname=fullname, discription=discription)
        c.save()

        return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def news(request):
    return render(request, 'news.html')
