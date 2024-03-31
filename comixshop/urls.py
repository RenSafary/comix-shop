from django.urls import path
from .views import *


urlpatterns = [
    path('', Main.as_view(), name="main"),
    path("manga/", manga),
    path("manhwa/", manhwa),
    path("manhua/", manhua),
    path('auth/', auth),
    path("books/", Book.as_view(), name="products"),
    path("books/remove/", Book.as_view(), name="delete"),
    path("books/edit/", Book.as_view(), name="edit"),
    path('books/add/', add, name="prods add"),
    path("logout/", logout_),
]