from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User



def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

# if password match
        if password == password2 :
            
            if User.objects.filter(username=username).exists():
                messages.error(request,'this username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'this email already exists')
                    return redirect('register')
                else:
                    User.objects.create_user(first_name=first_name,username=username,last_name=last_name,
                    email=email,password=password).save()
                    
                    messages.success(request,'you are succesfully registered and can now log in')
                    return redirect('login')


        else:
            messages.error(request,'passwords do not match')
            return redirect ('register')
    else:

        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'ivalid input')
            return redirect('login')
    else:
        return render(request,'login.html')
    

def dashboard(request):
    return render(request,'dashboard.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'you are succesfully loggedout')
    return render(request,'index.html')
    
