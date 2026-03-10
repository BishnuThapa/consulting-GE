from django.shortcuts import get_object_or_404, render
from aboutus.models import *
from slider.models import *
from django.http import HttpResponse
from faq.models import Faq
from destination.models import Destination
# Create your views here.


def index(request):
    slider=Slider.objects.first()
    about=About.objects.first()
    context={
        'slider': slider,
        'about': about,
    }
    return render(request, 'index.html',context)


def faq(request):
    faqs=Faq.objects.filter(is_active=True).order_by('ordering')
    context={
        'faqs': faqs,
    }
    return render(request, 'faq.html',context)


def destination_detail(request, slug):
    single_destination = get_object_or_404(Destination, slug=slug)
    all_destinations = Destination.objects.all()  # get all destinations for sidebar
    context = {
        'single_destination': single_destination,
        'destinations': all_destinations,  # pass to template
    }

    return render(request, 'destination-detail.html', context)


def contact(request):
    return render(request, 'contact.html')



# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save to DB
#         CustomerInquiry.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             subject=subject,
#             message=message,
#         )
#         return HttpResponse('<p class="text-success">Your message has been sent successfully!</p>')
#     return render(request, 'contact.html')


# def error_404(request, exception):
#     return render(request, '404.html')
