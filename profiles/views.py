from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.base import TemplateView
from .models import UserProfile
from blog.models import Post, Comment
from django.db.models import Count, Q
from .forms import EditProfileForm
from django.contrib import messages


class UserAccount(TemplateView):

    """A view to show the user account page"""

    template_name = 'user_account.html'


class ViewProfile(TemplateView):

    """A view for users to access their own profile page"""

    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context["user_profile_data"] = UserProfile.objects.filter(user=current_user)[0]
        
        return context


class ViewPublicProfile(View):

    """A view for users to view another users profile"""

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

    """A view for users edit their own profile"""

    model = UserProfile
    form_class = EditProfileForm
    template_name = 'edit_user_profile.html'

    def form_valid(self, form):
        if form.is_valid():
            messages.add_message(self.request, messages.SUCCESS, "Your profile was edited successfully.")
        else:
            messages.add_message(self.request, messages.ERROR, "Ooops, something went wrong. Please try again!")

        return super().form_valid(form)


class ViewUserPosts(TemplateView):

    """A view for users to view their own draft and published posts"""

    template_name = 'user_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        approved_comments = Count('comments', filter=Q(comments__approved=True))
        user_posts = Post.objects.filter(author=current_user).annotate(approved_comments=approved_comments).order_by('-created_on')
        published_posts = user_posts.filter(status=1)
        draft_posts = user_posts.filter(status=0)

        context = {
            'published_posts': published_posts,
            'draft_posts': draft_posts,
        }

        return context
