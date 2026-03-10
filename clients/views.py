from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def university(request):
    universities=Client.objects.all()
    

    context = {
        'universities': universities,

    }
    return render(request, 'university.html', context)
