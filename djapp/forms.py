from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        # is_staff = forms.BooleanField(required=True, initial=True)
        model = User
        fields = ('username', 'email', 'password1','password2','is_staff')


class UForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2','is_superuser','is_staff')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'is_superuser':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff' : forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class PForm(forms.ModelForm):
    Post_category = forms.ModelChoiceField(
        queryset= Category.objects.all(),
            empty_label="Select Category",
            widget =forms.Select(
                attrs=
                {
                    "class": "form-control selectpicker",
                    "type": "text",
                    "name": "category",
                    "id": "category",
                    "data-live-search": "true"
                }
            )
        )
    
    x = []
    for i in Tag.objects.all() :
        x.append(i.Name)
    Tags = forms.CheckboxSelectMultiple(x)
    
    class Meta:
        model = Post
        fields = ('Title','Picture','Content','Post_category','Tags','User_id')
        widgets = {
            'Title': forms.TextInput(
                attrs={
                    'name': "article-title",
                    'class': "form-control",
                    'placeholder': "Enter Post Title",
                    'id': "articleTitle"
                }),

            'Picture': forms.FileInput(
                attrs={
                    "class": "form-control clearablefileinput",
                    "type": "file",
                    "id": "PostImg",
                    "name": "PostImg"
                }
            ),
            
            'Content': forms.Textarea(
                    attrs={
                        "rows": 5, "cols": 20,
                        'id': 'content',
                        'name': "article_content",
                        'class': "form-control",
                    }
            ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('Text',)
        
        def __str__(self):
            return f"{self.Text} by {self.User_id}"

class BadWordsForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('Name',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('Name',)      
