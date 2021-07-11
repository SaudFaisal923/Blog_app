from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Profile,Blog,comments

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    created_date=forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
class CreateBlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('blog_title','blog_description')

class CommentForm(forms.ModelForm):
    class Meta:
        model=comments
        fields=('Comment',)
