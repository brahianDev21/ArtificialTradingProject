from django.urls import path
from .views import dashboard

urlpatterns = [
    path('overview', dashboard, name='dashboard'),
]