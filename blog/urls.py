from django.urls import path
from . import views

# app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    # path('blogs/load-more/', views.load_more_blogs, name='load-more-blogs'),
    # path('<slug:slug>', views.blog_detail, name='blog-detail'),
    # path('category/<slug:slug>', views.blog_category, name='blog-category'),
]