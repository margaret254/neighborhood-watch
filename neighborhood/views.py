from django.shortcuts import render
from .models import *

def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'main/index.html', {'hoods':hoods})

def hood(request,id):
    hoods = Neighborhood.objects.get(id=id)

    
    return render(request, 'main/hood.html', {'hoods':hood})