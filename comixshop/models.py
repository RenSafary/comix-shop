from django.db import models


class Books(models.Model):
    image = models.ImageField(upload_to="images/")
    type = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=150, blank=True)
    volume = models.IntegerField()
    genre = models.TextField(blank=True)
    description = models.TextField(blank=True)
    pages = models.IntegerField()
    amount = models.IntegerField()
    count_viewed = models.IntegerField() # delete