from django.shortcuts import render, redirect

from garbage.models import Member

def mark_area(request):
    return render(request, 'mark_area.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_member = Member(username=username)
        new_member.password = password
        new_member.save()
        return redirect('/')
    return render(request, 'authentication/register.html')


def login(request):
    return render(request, 'authentication/login.html')


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def details(request):
    return render(request,'details.html')

def login_interface(request):
    return render(request,'login_interface.html')