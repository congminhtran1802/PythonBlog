from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.template import loader
from blog.models import New
from django.db.models import Q
# Create your views here.

def contact(request):
    first_id = New.objects.first().id
    context = {
        'activecontact' : 'contact',
        'first_id': first_id
    }
    return render(request,'page/about.html', {'context' : context})

def home(request):
    first_id = New.objects.first().id
    search_query = request.GET.get('search', '')
    if search_query:
        News = New.objects.filter(Q(tittle__icontains=search_query))
        paginator = Paginator(News, 5)  # Hiển thị 5 bài đăng trên mỗi trang
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    else:
        News = New.objects.all().order_by('-created_at')
        paginator = Paginator(News, 5)  # Hiển thị 5 bài đăng trên mỗi trang
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    ids = list(New.objects.values_list('id', flat=True))
    context ={
        'News':posts,
        'activehome' : 'home',
        'first_id': first_id,
    }
    return render(request,'page/blog-list.html',{'context' : context})

def blog_detail(request,id):
    first_id = New.objects.first().id
    News = New.objects.get(id=id)
    current_id = News.id
    ids = list(New.objects.values_list('id', flat=True))
    next_id = -1
    pre_id = -1
    if current_id in ids:
        current_index = ids.index(current_id)
        if current_index + 1 < len(ids):
            next_id = ids[current_index + 1]
        if current_index - 1 >= 0:
            pre_id = ids[current_index - 1]
    body = News.body.replace('\\n', '<br>')
    split_str = '...'
    body_parts = body.split(split_str)
    body_image = []
    if len(body_parts) > 1:
        for i in range(len(body_parts)):
            if i+1 < len(News.images.all()):
                body_image.append({"body":body_parts[i],"image":News.images.all()[i+1]})
            else:
                body_image.append({"body":body_parts[i],"image":None})
    context = {
        'News': News,
        'body_image': body_image,
        'next_id': next_id,
        'pre_id': pre_id,
        'activeblog' : 'blog',
        'first_id': first_id,
    }
    return render(request,'page/blog-post.html',{'context':context})
    

