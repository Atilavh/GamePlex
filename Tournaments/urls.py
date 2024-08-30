from django.urls import path
from . import views

urlpatterns = [
    path('tournament_list/', views.tournament_list, name='tournament_list'),
    path('image_save/', views.tournament_image_save, name='image'),
]