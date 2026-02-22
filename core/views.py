from django.shortcuts import render
from aboutus.models import *
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

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
