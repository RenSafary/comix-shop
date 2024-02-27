from django.urls import path
from .views import *


urlpatterns = [
    path('', main),
    path('auth/', auth),
    path("products/", Products.as_view(), name="products"),
    path("products/remove/", Products.as_view(), name="delete"),
    path("products/edit/", Products.as_view(), name="edit"),
    path("logout/", logout_),
    path('add/', add),
]