from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalis credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check password
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email has used already')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email, 
                    first_name= first_name, last_name = last_name)
                    # auth.login(request, user)
                    # return redirect('index')
                    user.save()
                    return redirect('login')
        else:
            messages.error(request,'password does not match')
            return redirect('register')
    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    contacts = Contact.objects.all().filter(user_id = request.user.id )
    return render(request, 'accounts/dashboard.html',context = {
        'contacts': contacts
    })