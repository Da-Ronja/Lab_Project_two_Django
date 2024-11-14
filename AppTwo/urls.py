from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('web_table/', views.web_table, name='web_table'),
]