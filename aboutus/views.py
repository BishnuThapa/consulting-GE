from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def about(request):

    about = About.objects.first()
    context = {
        'about': about,

    }
    return render(request, 'about.html', context)


def chairmanmessage(request):
    chairman_message = ChairmanMessage.objects.first()
    context = {
        'chairman_message': chairman_message,

    }
    return render(request, 'md-message.html', context)



def whyus(request):

    whyus = WhyUs.objects.first()
    context = {
        'whyus': whyus,

    }
    return render(request, 'why-us.html', context)


