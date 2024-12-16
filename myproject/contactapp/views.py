from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from .models import Contact

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Model ma data store garna
        Contact.objects.create(name=name, email=email, message=message)
        
        return redirect('index')  # Form submit vaye pachi same page ma redirect

    return render(request, 'contactapp/index.html')


def send_email_notification(contact):
    send_mail(
        'New Contact Form Submission',
        f'You have a new message from {contact.name} ({contact.email}).\n\nMessage: {contact.message}',
        'irachand620@gmail.com',  # Admin email address
        ['irachand620@gmail.com'],  # Recipient's email
    )