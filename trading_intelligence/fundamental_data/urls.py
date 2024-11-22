from django.urls import path
from .views import fundamentalData

urlpatterns = [
    path('fundamental_data/', fundamentalData, name='fundamental_data'),
]
