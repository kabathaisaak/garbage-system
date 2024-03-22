from django.urls import path
from .views import garbage_request_list, create_garbage_request
from .views import company_registration,CompanyLoginView

urlpatterns = [
    path('requests/', garbage_request_list, name='garbage_request_list'),
    path('create/', create_garbage_request, name='create_garbage_request'),
    path('register/', company_registration, name='company_registration'),
    path('company_login/', CompanyLoginView.as_view(), name='company_login'),

]

