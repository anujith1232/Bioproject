from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect

# Create your views here.
def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('view')
        else:
            messages.info(request, 'Please provide correct details')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def profileview(request):
    return render(request,"profile view.html")

