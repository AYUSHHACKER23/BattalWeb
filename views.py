from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact 
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'Services.html')

from .models import Contact as ContactModel

def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        contact = ContactModel(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request, 'Contact.html')

