from django.urls import path
from . import views
from services.views import service, service_detail
from aboutus.views import about, chairmanmessage, whyus
from page.views import page


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', about, name='about'),
    # path('vision-mission/', vision, name='vision'),
    # path('md-message/', chairmanmessage, name='md-message'),
    # path('certification/', certification, name='certification'),
    # path('company-profile/', profile, name='profile'),
    # path('available-job/', views.job, name='jobs'),
    # path('services/<slug:slug>/', service_detail, name='service-detail'),
    # path('company/<slug:slug>/', howwedo_detail, name='howwedo-detail'),
    path('<slug:slug>/', page, name="page-detail"),
    path('contact-us', views.contact, name='contact'),
    # Add other URL patterns here
]