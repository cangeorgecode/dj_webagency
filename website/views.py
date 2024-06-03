from django.shortcuts import render
from .models import *

def index(request):
    websites = Website.objects.all()
    return render(request, 'website/index.html', {'websites': websites})

def portfolio(request, id):
    website = Website.objects.get(id=id)
    return render(request, 'website/portfolio.html', {'website': website})
