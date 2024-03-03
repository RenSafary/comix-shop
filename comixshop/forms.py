from django import forms
from .models import Books


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['image', 'title', 'volume', 'genre', 'description', 'pages', 'amount']
        labels = {
            'image': 'Изображение',
            'title': 'Название',
            'volume': 'Том',
            'genre': 'Жанр',
            'description': 'Описание',
            'pages': 'Страниц',
            'amount': 'Кол-во (шт.)',
        }