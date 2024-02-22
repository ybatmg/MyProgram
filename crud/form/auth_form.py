from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,label='Username',required=True,error_messages={'required':'Please enter username.'})
    password=forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput,required=True,error_messages={'required':'Please enter password.'})

class SignupForm(forms.Form):
    username=forms.CharField(max_length=50,label='Username',required=True,error_messages={'required':'Please enter username.'})
    email=forms.CharField(max_length=100,label='Email',required=True,error_messages={'required':'Please enter email.'})
    password=forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput,required=True,error_messages={'required':'Please enter password.'})
