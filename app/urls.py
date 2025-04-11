from django.urls import path
from .views import veiwproducts ,download_db ,download_media
urlpatterns = [
    path('products/',veiwproducts, name='viewproducts'),
    path('downloaddbxxv/1386/', download_db, name='download_db'),
    path('downloadmediaxxv/67492/', download_media, name='downloadmedia')
]
