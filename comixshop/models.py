from django.db import models


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)


class Book(models.Model):
    #image = models.ImageField()
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=10)
    description = models.TextField()
    pages = models.IntegerField()
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    views = models.IntegerField()
    amount = models.IntegerField()
    sales = models.IntegerField()