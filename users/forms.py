from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from . models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user_name', 'post_title', 'post_content', 'date_published', 'user_profile_link']