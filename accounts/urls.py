from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('', register, name='register'),
    path('profile/', profile, name='profile'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]