from .models import Post, Comment
from django import forms
from allauth.account.forms import SignupForm, LoginForm, AddEmailForm, ChangePasswordForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):

    """Fields and styles for creating a post"""

    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'slug', 'content', 'excerpt', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter a post title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-lg',  'placeholder': 'Enter a post slug'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'content': SummernoteWidget(),
            'excerpt': forms.Textarea(attrs={'class': 'form-control form-control-lg excerpt-height',  'placeholder': 'Enter a short summary of the post'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg form-select'}),
        }


class EditForm(forms.ModelForm):

    """Fields and styles for editing a post"""

    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'slug', 'content', 'excerpt', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter a post title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-lg',  'placeholder': 'Enter a post slug'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'content': SummernoteWidget(),
            'excerpt': forms.Textarea(attrs={'class': 'form-control form-control-lg excerpt-height', 'placeholder': 'Enter a short summary of the post'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg form-select'}),
        }


class CommentForm(forms.ModelForm):

    """Fields for the post comments"""

    class Meta:
        model = Comment
        fields = ('body',)


class SigninForm(LoginForm):

    """Fields and styles for the sign in form"""

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})


class RegisterForm(SignupForm):

    """Fields and styles for the sign up form"""
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})


class PasswordForm(ChangePasswordForm):

    """Fields and styles for the change password form"""

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})


class EmailForm(AddEmailForm):

    """Fields and styles for the add/edit email form """

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control form-control-lg'})
