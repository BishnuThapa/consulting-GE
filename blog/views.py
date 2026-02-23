from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def blog(request):
   
    # blogs = Blog.objects.all().order_by('-id')[:3]
    # context={
    #     'blogs':blogs,
        # 'banner':banner,
        # 'categories': categories,
    # }
    return render(request, 'blog.html')
    
# def load_more_blogs(request):
#     offset = int(request.GET.get('offset', 0))
#     limit = int(request.GET.get('limit', 3))
#     blogs = Blog.objects.all().order_by('-id')[offset:offset+limit]
#     return render(request, 'partials/blog_list.html', {'blogs': blogs})

# def blog(request):
#     limit = 3  # number of blogs to load each time
#     blogs = Blog.objects.all().order_by('-id')[:limit]
#     context = {
#         'blogs': blogs,
#         'limit': limit,  # pass limit to template
#     }
#     return render(request, 'blog.html', context)

# def load_more_blogs(request):
#     offset = int(request.GET.get('offset', 0))
#     limit = int(request.GET.get('limit', 3))
#     blogs = Blog.objects.all().order_by('-id')[offset:offset+limit]
#     return render(request, 'partials/blog_list.html', {'blogs': blogs})
# from django.http import HttpResponse
# from django.http import HttpResponse

# def blog(request):
#     categories = Category.objects.all()
#     limit = 6
#     blogs = Blog.objects.all().order_by('-id')[:limit]
#     total_blogs = Blog.objects.count()
    
#     context = {
#         'blogs': blogs,
#         'categories':categories,
#         'limit': limit,
#         'total_blogs': total_blogs,
#         'has_more': total_blogs > limit,
#         'next_offset': limit  # Initial offset for next load
#     }
#     return render(request, 'blog.html', context)

# def load_more_blogs(request):
#     offset = int(request.GET.get('offset', 0))
#     limit = int(request.GET.get('limit', 3))
    
#     # Calculate the next offset
#     next_offset = offset + limit
    
#     # Get blogs for current offset
#     blogs = Blog.objects.all().order_by('-id')[offset:next_offset]
    
#     # Check if we got any blogs
#     if not blogs.exists():
#         return HttpResponse(status=204)  # No Content
    
#     # Check if this is the last batch
#     total_count = Blog.objects.count()
#     is_last_batch = next_offset >= total_count
    
#     return render(request, 'partials/blog_list.html', {
#         'blogs': blogs,
#         'is_last_batch': is_last_batch,
#         'next_offset': next_offset
#     })

    
# def blog_detail(request, slug):
#     # banner = Banner.objects.first()
#     # blogseo=Seo.objects.first()
#     blog = get_object_or_404(Blog, slug=slug)
#     related_products = Blog.objects.all().order_by(
#         '-id').exclude(slug=slug)[:6]
#     context = {
#         'blog': blog,
#         # 'banner': banner,
#         # 'blogseo': blogseo

#         # 'categories': categories,
#         'related_products': related_products
#     }
#     return render(request, 'blog-detail.html', context)


# def blog_category(request, slug):
#     # banner = Banner.objects.first()
#     category = get_object_or_404(Category, slug=slug)
#     blogs = Blog.objects.filter(category__title=category)
#     context = {
#         'category': category,
#         'blogs': blogs,
#         # 'banner': banner
#     }
#     return render(request, 'blog-category.html', context)