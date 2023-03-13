from django import forms

class RegisterForm(forms.Form):
  username = forms.CharField(label="Username", widget=forms.TextInput())
  password = forms.CharField(label='Password', widget=forms.PasswordInput())
  password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())