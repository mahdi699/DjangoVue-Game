from django.urls import path
from .views import *

urlpatterns = [
    path('submit_score/', submit_score, name='submit_score'),
    path('scoreboard/', scoreboard, name='scoreboard'),
]