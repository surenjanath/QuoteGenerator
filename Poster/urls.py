"""Article URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('Generate', views.GenerateItem, name = 'Generate'),
]
