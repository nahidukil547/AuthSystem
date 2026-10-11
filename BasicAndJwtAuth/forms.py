from django import forms
from django.contrib.auth.models import User



class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField()
    class Meta:
        model = User
        fields = ("first_name",'last_name','email','username','password','confirm_password')
    