"""rauf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.register,name='signup'),
    path('login/',views.Login,name='login'),
    path('login/blogs/',views.Blogs,name='blogs'),
    path('login/blogs/<int:id>',views.View_blog,name='viewblog'),
    path('login/create/',views.create_blog,name='create_blog'),
    path('login/myblogs/',views.MyBlogs,name='myblogs'),

]
