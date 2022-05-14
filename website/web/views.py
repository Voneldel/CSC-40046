from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
import datetime
# Create your views here.

def index(request):
    current_datetime = datetime.datetime.now()  
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/index.html', {'time': current_datetime})

def login(request):
    current_datetime = datetime.datetime.now()  
    return render(request, 'web/login.html', {'time': current_datetime})

def home(request):
    current_datetime = datetime.datetime.now()  
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member, 'time': current_datetime})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
    else:
        return redirect('/')

