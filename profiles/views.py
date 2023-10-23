from django.views.generic.base import TemplateView
from .models import UserProfile


class ViewProfile(TemplateView):

    model = UserProfile
    template_name = 'user_profile.html'