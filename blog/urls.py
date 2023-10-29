from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', login_required(views.PostLike.as_view()), name='post_like'),
    path('new_post', login_required(views.AddPost.as_view()), name='add_post'),
    path('edit_post/<slug:slug>/', login_required(views.EditPost.as_view()), name='edit_post'),
    path('delete_post/<slug:slug>/', login_required(views.DeletePost.as_view()), name='delete_post'),
]
