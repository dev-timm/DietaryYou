from .models import UserProfile
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'profile_image', 'bio', 'hobbies', 'location')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your full name'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'bio': forms.Textarea(attrs={'class': 'form-control form-control-lg excerpt-height', 'placeholder': 'Enter a short summary about yourself'}),
            'hobbies': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your hobbies'}),
            'location': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your location'}),
        }
