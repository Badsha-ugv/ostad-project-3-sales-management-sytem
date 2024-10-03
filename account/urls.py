from django.urls import path 
from . import views 

app_name = 'account'

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('otp-verify/', views.otp_view, name='otp_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

]

