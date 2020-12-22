from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Contact
from django.contrib.auth.models import User
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # CHECK IF INQUIRY ALREADY EXIST

        if request.user.is_authenticated:
            user_id = user_id # or request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.info(request, "Sorry you")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing = listing, listing_id = listing_id,
        name = name, email = email, phone = phone, message = message, user_id = user_id)

        contact.save()

        messages.success(request, "Your request has been submitted")
        return redirect('/listings/'+listing_id)