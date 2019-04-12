from django.contrib import admin
from .models import User


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'last_login')
