from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('notes/', include('notes.urls')),
    path('', lambda request: redirect('register')),  # Redirect to register by default
]
