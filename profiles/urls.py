from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('user_account', login_required(views.UserAccount.as_view()), name='user_account'),
    path('user_profile', login_required(views.ViewProfile.as_view()), name='user_profile'),
    path('user_posts', login_required(views.ViewUserPosts.as_view()), name='user_posts'),
    path('<slug:slug>/', views.ViewPublicProfile.as_view(), name='public_user_profile'),
    path('edit_profile/<slug:slug>/', login_required(views.EditProfile.as_view()), name='edit_profile'),
]
