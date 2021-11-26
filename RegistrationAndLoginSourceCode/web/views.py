from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.



def sitemap(request):
    return render(request, 'web/sitemap.html')

<<<<<<< HEAD:RegistrationAndLoginSourceCode/web/views.py
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
=======

>>>>>>> 83d1d6f (IRS sitemap task):web/views.py

