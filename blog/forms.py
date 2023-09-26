from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'slug', 'author', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'author': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg'}),            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
