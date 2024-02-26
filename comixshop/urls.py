from django.urls import path
from .views import *


urlpatterns = [
    path('', main),
    path('auth/', auth),
    path("products/", Products.as_view(), name="products"),
    path("products/remove/", Products.as_view(), name="delete"),
]