from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from .models import UserProfile


class UserAccount(TemplateView):

    template_name = 'user_account.html'


class ViewProfile(TemplateView):

    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context["user_profile_data"] = UserProfile.objects.filter(user=current_user)[0]
        
        return context


class ViewPublicProfile(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = UserProfile.objects.all()
        user_profile_data = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "public_user_profile.html",
            {
                "user_profile_data": user_profile_data,
            },
        )
