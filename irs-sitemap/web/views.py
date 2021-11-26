from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.



def sitemap(request):
    return render(request, 'web/sitemap.html')



