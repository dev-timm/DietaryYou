from django.views.generic.base import TemplateView
from blog.models import Post, Comment
from django.db.models import Count, Q


class ViewHomepage(TemplateView):

    """A view to show the homepage containing the 3 most liked and recent posts"""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.filter(status=1).annotate(approved_comments=Count('comments', filter=Q(comments__approved=True))).order_by('-created_on')[:3]
        popular_posts = Post.objects.filter(status=1).annotate(approved_comments=Count('comments', filter=Q(comments__approved=True), distinct=True)).annotate(likes_count=Count('likes', distinct=True)).order_by('-likes_count')[:3]

        context = {
            'latest_posts': latest_posts,
            'popular_posts': popular_posts
        }

        return context
