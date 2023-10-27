from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.base import TemplateView
from .models import UserProfile
from .forms import EditProfileForm
from django.contrib import messages


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


class EditProfile(generic.UpdateView):

    model = UserProfile
    form_class = EditProfileForm
    template_name = 'edit_user_profile.html'

    def form_valid(self, form):
        if form.is_valid():
            messages.add_message(self.request, messages.SUCCESS, "Your profile was edited successfully.")
        else:
            messages.add_message(self.request, messages.ERROR, "Ooops, something went wrong. Please try again!")

        return super().form_valid(form)
