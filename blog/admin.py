from django.contrib import admin
from blog.models import Profile,Blog,comments
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(comments)
