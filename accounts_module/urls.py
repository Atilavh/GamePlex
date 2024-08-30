from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.register_page, name='Register'),
    path('login/', views.login_page, name='Login'),
    path('forgot/', views.forgot_password_page, name='Forgot'),
    path('logout/', views.logout_page, name='Logout'),

    path('activate-account/<email_code>', views.ActivateAccountView.as_view(), name='active_page')
]
