from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth
from django.contrib.auth.models import User
from form.auth_form import LoginForm,SignupForm

# Create your views here.
def login(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                auth(request,user)
                return redirect('home')
            else:
                login_form.add_error('username','Username or Password is incorrect!!')
                return render(request,'login.html',{'form':login_form})
    login_form=LoginForm()    
    return render(request,'login.html',{'form':login_form})

def signup(request):
    if request.method=="POST":
        print('wdawdwad')
        signup_form=SignupForm(request.POST)
        if signup_form.is_valid():
            print(signup_form.cleaned_data)
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            user = User.objects.create_user(username=username,email=email,password=password)
            if user:
                user.save()
                return redirect('login')
            else:
                signup_form.add_error('username','Something went wrong, Please try again.')
                return render(request,'signup.html',{'form':signup_form})

    signup_form=SignupForm()
    return render(request,'signup.html',{'form':signup_form})

def home_view(request):
    return render(request,'home.html')