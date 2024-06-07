from . import views
from django.urls import path

app_name = 'jobportal'



urlpatterns = [
    

    # urls for function based views
    

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('ForgotPassword/',views.ForgotPassword,name='ForgotPassword'),
    
    
    # urls for class based views
    

    path('homeview/',views.HomeView.as_view(),name='homeview'),
    path('aboutview/', views.AboutView.as_view(),name='aboutview'),
    path('contactview/',views.ContactView.as_view(),name='contactview'),
    path('registerview/',views.RegisterView.as_view(),name='registerview'),
    path('loginview/',views.LoginView.as_view(),name='loginview'),
    path('ForgotPasswordView/',views.ForgotPasswordView.as_view(),name='ForgotPasswordView/'),
    





]











