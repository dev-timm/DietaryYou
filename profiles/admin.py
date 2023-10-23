from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class PostAdmin(admin.ModelAdmin):

    list_display = ('user', 'full_name', 'location', 'slug')
    search_fields = ['full_name', 'bio', 'hobbies', 'location']
    list_filter = ('full_name', 'hobbies', 'location')
