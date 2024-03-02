from django.urls import path
from .views import *


urlpatterns = [
    path('', Main.as_view(), name="main"),
    path('auth/', auth),
    path("products/", Products.as_view(), name="products"),
    path("products/remove/", Products.as_view(), name="delete"),
    path("products/edit/", Products.as_view(), name="edit"),
    path('products/add/', add, name="prods add"),
    path("logout/", logout_),
]