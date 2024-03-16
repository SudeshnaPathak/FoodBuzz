from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address',)  # Change this to a tuple

    def user(self, obj):
        return obj.user.username  # Change this to obj.user.username