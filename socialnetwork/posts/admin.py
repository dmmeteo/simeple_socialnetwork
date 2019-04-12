from django.contrib import admin
from .models import Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'sum_likes', 'sum_unlikes', 'text', 'release_date',)
