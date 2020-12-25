from django import forms
from app.models import *

class InitialRegistrationForm(forms.Form):
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": '例）山田'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": '例）太郎'}))
    acount_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20 ,widget=forms.PasswordInput(attrs={'pattern': '(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{6,}'}))
    password2 = forms.CharField(max_length=20 ,widget=forms.PasswordInput(attrs={'pattern': '(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{6,}'}))
    email_address = forms.EmailField(max_length=50)