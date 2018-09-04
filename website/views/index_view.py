from django.shortcuts import render
from django.template import RequestContext
# from website.models import Product



def index(request):
    return render(request, 'site/index.html', {})
