from django.urls import path
from .views import veiwproducts
urlpatterns = [
    path('products/',veiwproducts, name='viewproducts')
]
