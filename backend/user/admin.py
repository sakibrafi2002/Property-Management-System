from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nid', 'members', 'adults', 'women')  # Display fields in admin list view
    search_fields = ('nid',)  # Enable searching by NID
    list_filter = ('members',)  # Add filter for the number of members
