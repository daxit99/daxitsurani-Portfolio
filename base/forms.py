from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets

from .models import Post

class PostForm(ModelForm):

    class Meta:
        model=Post
        fields='__all__'

        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
