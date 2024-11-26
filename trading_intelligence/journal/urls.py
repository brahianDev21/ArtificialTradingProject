from django.urls import path, include
from rest_framework import routers
from .api import JournalViewSet

router = routers.DefaultRouter()
router.register(r'api', JournalViewSet, basename='journal')

urlpatterns = [
    path('', include(router.urls)),
]