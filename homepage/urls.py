from . import views
from django.urls import path

urlpatterns = [
    path('', views.ViewHomepage.as_view(), name='home'),
]
