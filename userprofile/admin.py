from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')
    exclude = ('date_created', )


admin.site.register(UserProfile, UserProfileAdmin)
