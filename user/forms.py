from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django import forms

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Nickname...'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'First Name...'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Last name...'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'type':'email', 'placeholder':'Email...'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'placeholder':'password', 'id':'pass'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'id':'pass2', 'type':'password', 'placeholder':'Password check...'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'placeholder':'Nickname...'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password', 'placeholder':'password', 'id':'pass'}))


    class Meta:
        model = User
        fields = ('username', 'password')


class UserPortfileForm(UserChangeForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={}))
    image = forms.ImageField(widget=forms.FileInput(attrs={}))

    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'email','image')
