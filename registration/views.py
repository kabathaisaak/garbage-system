from django.shortcuts import render, redirect
from .models import GarbageRequest, CompanyRegistrationModel
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib import auth



def garbage_request_list(request):
    garbage_requests = GarbageRequest.objects.all()
    return render(request, 'registration/request_list.html', {'garbage_requests': garbage_requests})


def create_garbage_request(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        GarbageRequest.objects.create(location=location)
        return redirect('garbage_request_list')
    return render(request, 'registration/create_request.html')


def company_registration(request):
        if request.method == 'POST':
            company_name = request.POST.get('company_name')
            company_contact_person = request.POST.get('company_contact_person')
            company_email = request.POST.get('company_email')
            company_phone_number = request.POST.get('company_phone_number')
            company_ID = request.POST.get('company_ID')
            company_description = request.POST.get('company_description')
            company_password = request.POST.get('company_password')

            if not company_name or not company_email or not company_password:
                return HttpResponse("Please fill in all required fields.")

            CompanyRegistrationModel.objects.create(
                company_name=company_name,
                company_contact_person=company_contact_person,
                company_email=company_email,
                company_phone_number=company_phone_number,
                company_ID=company_ID,
                company_description=company_description,
                company_password=company_password
            )

            return HttpResponse(f'Thank you, {company_name}, for registering!')

        return render(request, 'registration/register.html')






class CompanyLoginView(View):
        def get(self, request):
            return render(request, 'registration/company_login.html')

        def post(self, request):
            Company_ID = request.POST['Company_ID']
            password = request.POST['password']

            if Company_ID and password:
                user = auth.authenticate(Company_ID=Company_ID, password=password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        messages.success(request, 'Welcome ' + Company_ID + ' you are logged in successfully')
                        return redirect('index')
                    else:
                        messages.error(request, 'Account not activated please check your email')
                else:
                    messages.error(request, 'Username or password is invalid!')
            else:
                messages.error(request, 'Please enter Company_ID and password!')
            return render(request, 'index.html')