
from django.contrib import admin
from django.urls import path,include
from garbage import views

urlpatterns = [
    path('', include('garbage.urls')),
    path('', include('authentication.urls')),
    path('registration/', include('registration.urls')),
]
