from django.shortcuts import render
from .models import Advertisment
# from django.http import HttpResponse

# Create your views here.

def index(request):
    adverts=Advertisment.objects.all()
    context={"advert":adverts}
    return render(request, 'index.html', context)

def topSellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

