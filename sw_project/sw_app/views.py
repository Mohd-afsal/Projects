from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from . models import resources

# Create your views here.


def goto_index(request):
    sampl_img = resources.objects.all()
    return render(request, 'index.html', {'obj': sampl_img})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Please check username & password")
            return redirect(request, 'login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if username == '' or first_name == '' or last_name == '' or email == '' or password == '' or cpassword == '':
            messages.info(request, "Please enter all fields")
            return redirect('register')
        else:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username is taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already registered")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    email=email,
                                                    password=password)
                    user.save()
                    messages.info(request, "User Created")
                    return redirect('login')
            else:
                messages.info(request, "Passwords not matching")
                return redirect('register')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def contact(request):
    return render(request, 'contact.html')
