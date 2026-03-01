from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def client_detail(request, slug):

    single_client = get_object_or_404(Client, slug=slug)

    context = {
        'single_client': single_client,


    }
    return render(request, 'client-detail.html', context)
