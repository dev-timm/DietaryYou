from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('user_account', login_required(views.UserAccount.as_view()), name='user_account'),
    path('user_profile', login_required(views.ViewProfile.as_view()), name='user_profile'),
    path('<slug:slug>/', views.ViewPublicProfile.as_view(), name='public_user_profile'),
]
