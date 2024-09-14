from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

# Create your views here.

def index_post(request):
    items_per_page = request.GET.get('items_per_page', 1)
    items = Post.objects.all().order_by('-created_id')
    paginator = Paginator(items, items_per_page)
    # posts = Post.objects.all().order_by('-created_id')
    # paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(items_per_page)
    # print(page_number)
    # print(page_obj)
    return render(request, 'index_post.html', {'page_obj': page_obj, 'items_per_page': int(items_per_page)})
