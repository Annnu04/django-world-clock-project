from django.urls import path
from .views import world_clock

urlpatterns = [
    path('', world_clock, name='world_clock'),
]
