from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.contrib import messages
from django.db.models import Count, Q


class PostList(generic.ListView):

    """A view to show a list of all posts and the number of comments"""

    model = Post
    template_name = 'blog.html'

    paginate_by = 6

    def get_queryset(self):
        approved_comments = Count('comments', filter=Q(comments__approved=True))
        queryset = Post.objects.filter(status=1).annotate(approved_comments=approved_comments).order_by('-created_on')
        return queryset

    context_object_name = 'post_list'


class AddPost(generic.CreateView):

    """A view to create a new post with the author being the signed in user """

    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # solution created with the help from https://www.reddit.com/r/djangolearning/comments/l7nuah/how_to_automatically_add_the_logged_in_users/
    def form_valid(self, form):
        if form.is_valid():
            form.instance.author = self.request.user
            messages.add_message(self.request, messages.SUCCESS, "Your post was published successfully.")
        else:
            messages.add_message(self.request, messages.ERROR, "Ooops, something went wrong. Please try again!")

        return super().form_valid(form)


class EditPost(generic.UpdateView):

    """A view to edit a post"""

    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

    def form_valid(self, form):
        if form.is_valid():
            messages.add_message(self.request, messages.SUCCESS, "Your post was edited successfully.")
        else:
            messages.add_message(self.request, messages.ERROR, "Ooops, something went wrong. Please try again!")

        return super().form_valid(form)


class DeletePost(generic.DeleteView):

    """A view to delete a post"""

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    # solution created with the help from https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, "Your post was deleted successfully.")
        return super(DeletePost, self).delete(request, *args, **kwargs)


class PostDetail(View):

    """A view to view a post and like/comment on it"""

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(self.request, messages.SUCCESS, "Your comment was submitted and is awaiting approval.")
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    """A view to like a post"""

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
