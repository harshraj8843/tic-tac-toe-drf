from django.urls import path
from . import views

urlpatterns = [
    path('play/', views.play.as_view(), name='play'),
]