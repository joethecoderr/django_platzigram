from django import forms
from django.contrib.auth.models import User
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'photo')

