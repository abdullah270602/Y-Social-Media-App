from django import forms
from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    body = forms.CharField(max_length=256, required=True)
    class Meta:
        model = Post
        fields = ('body',)