from django.contrib import admin
from django.urls import path
from garbage import views
from garbage.views import mark_area

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('details/', views.details, name='details'),
    path('login_interface', views.login_interface, name='login_interface'),
    path('', mark_area, name='mark_area'),

]
