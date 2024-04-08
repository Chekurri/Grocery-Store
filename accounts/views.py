from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


"""This function loads the home page"""
def load_home(request):
    return render(request, 'home.html')

"""
This function is used to load the about us page
"""
def about_us(request):
    return render(request, 'about_us.html')

"""
This function is used to login  user
"""
def login_user(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        userObj = auth.authenticate( username=user_name, password=password)
        if userObj is not None:
            auth.login(request, userObj)
            request.session['user_id'] = userObj.id
            request.session['username'] = userObj.username
            return redirect('/website')
        else:
            messages.error(request, 'Username/password is wrong')
            return redirect('/login')
    else:
        return render(request, 'login.html')

"""
This function is used to register the new user and save the data 
to database"""
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email_id = request.POST['email']

        if pass1 == pass2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Already Taken!')
                return redirect('/register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, 'Email id Already Taken')
                return redirect('/register')
            else:
                userObj = User.objects.create_user(username=user_name, password=pass1, email=email_id,
                                                first_name=first_name,
                                                last_name=last_name)
                userObj.save()
                return redirect('/login')
        else:
            messages.info(request, 'Passwords does not match')
            return redirect('/register')
    else:
        return render(request, 'register.html')


"""Function to logout the user"""
def logout(request):
    auth.logout(request)
    return redirect('/')
