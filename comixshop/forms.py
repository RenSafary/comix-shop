from django import forms
from .models import Books, Genres


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['image', 'title', 'type', 'description', 'pages', 'views', 'amount', 'sales', 'genre']
        labels = {
            'image': 'Изображение',
            'title': 'Название',
            'type': 'Тип',
            'description': 'Описание',
            'pages': 'Страниц',
            'view': 'Просмотров',
            'amount': 'Кол-во (шт.)',
            'sales': 'Продаж',
            'genre': 'Жанр',
        }