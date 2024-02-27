from django import forms
from .models import Books


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['image']