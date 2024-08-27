from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.register_page, name='Register'),
    path('login/', views.login_page, name='Login'),

    path('activate-account/<email_code>', views.ActivateAccountView.as_view(), name='active_page')
]
