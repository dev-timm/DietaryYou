from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('new_post', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<slug:slug>/', views.EditPost.as_view(), name='edit_post'),
    path('delete_post/<slug:slug>/', views.DeletePost.as_view(), name='delete_post'),
    path('user_account', views.UserAccount.as_view(), name='user_account'),
]
