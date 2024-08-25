from django.urls import path
from . import views

urlpatterns = [
    path('Register', views.register_page, name='Register'),
]