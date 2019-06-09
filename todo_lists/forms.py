from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'enter your username'}))
    password = forms.CharField(label='', widget=forms.TextInput(attrs=
    {'placeholder':'enter your password', 'type':'password'}))
