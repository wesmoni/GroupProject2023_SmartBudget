from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),  # http://127.0.0.1:8000/
]
