from django.views.generic.base import TemplateView
from blog.models import Post, Comment
from django.db.models import Count, Q


class ViewHomepage(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        approved_comments = Count('comments', filter=Q(comments__approved=True))
        latest_posts = Post.objects.filter(status=1).annotate(approved_comments=approved_comments).order_by('-created_on')[:3]
        popular_posts = Post.objects.filter(status=1).annotate(approved_comments=approved_comments).order_by('likes')[:3]

        context = {
            'latest_posts': latest_posts,
            'popular_posts': popular_posts
        }

        return context
