
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth. views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    # PasswordChangeView,
    # PasswordChangeDoneView,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('account.urls', namespace='account')),
    path('', include('index.urls', namespace='index')),


    # rest password url 
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete')
    
    
    
]
