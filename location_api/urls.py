from django.urls import path
from .views import get_locations

urlpatterns = [
    path('locations/', get_locations, name='get_locations'),
]