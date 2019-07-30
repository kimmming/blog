
from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/BlogH',blogapp.views.BlogH, name ="BlogH"),
    path('',blogapp.views.home,name="home"),
    
    path('blog/<int:blog_id>', blogapp.views.detail, name ="detail"),
    path('blog/new/',blogapp.views.new, name='new'),
    path('blog/create',blogapp.views.create, name ="create"),
]

