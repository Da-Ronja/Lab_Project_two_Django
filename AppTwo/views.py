from django.shortcuts import render, get_object_or_404
from AppTwo.models import AccessRecord, BlogPost

# Create your views here.
from django.http import HttpResponse


def index(request):
    my_dict = {'django_reinhardt': "This is Django on first_app/index.html!"}
    return render(request, 'first_app/index.html', context=my_dict)

def profile(request):
    return render(request, 'first_app/profile.html')

def help(request):
    return render(request, 'help.html')

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'first_app/blog.html', {'blog_posts': blog_posts})

def blog_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'first_app/blog_detail.html', {'blog_post': blog_post})

def web_table(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/web_table.html', context=date_dict)