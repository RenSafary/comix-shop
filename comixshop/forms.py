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
            'views': 'Просмотров',
            'amount': 'Кол-во (шт.)',
            'sales': 'Продаж',
            'genre': 'Жанр',
        }

    def __init__(self, *args, **kwargs): # не работает так
        super().__init__(*args, **kwargs)
        self.fields['genre'].queryset = Genres.objects.all()