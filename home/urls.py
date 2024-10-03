
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('account.urls', namespace='account')),
    path('', include('index.urls', namespace='index')),
    
    
]
