from django.shortcuts import render
from django.contrib.auth import get_user

def home(request):
    currentuser = get_user(request)
    return render(request, 'website/index.html', {"currentuser": currentuser} )
