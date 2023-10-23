from . import views
from django.urls import path

urlpatterns = [
    path('user_profile', views.ViewProfile.as_view(), name='user_profile'),
    path('user_account', views.UserAccount.as_view(), name='user_account'),
]
