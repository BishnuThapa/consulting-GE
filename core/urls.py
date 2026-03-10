from django.urls import path,include
from . import views
from services.views import service, service_detail
from aboutus.views import about, chairmanmessage, whyus
from page.views import page
from clients.views import university


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('about-us/', about, name='about'),
    path('universities/', university, name='university'),
    path('director-message/', chairmanmessage, name='md-message'),
    # path('certification/', certification, name='certification'),
    # path('company-profile/', profile, name='profile'),
    path('faq/', views.faq, name='faq'),
    path('services/<slug:slug>/', service_detail, name='service-detail'),
    path('destination/<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('<slug:slug>/', page, name="page-detail"),
    path('contact-us', views.contact, name='contact'),
    
    # Add other URL patterns here
]