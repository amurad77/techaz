from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group
from .models import Config

User = get_user_model()


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'image',
            'education',
            'position',
            'birthday',
            'status',
        )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'groups','user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


# @admin.register(Config)
# class ConfigAdmin(admin.ModelAdmin):
#     list_display = ("image", 'is_published')

admin.site.register(Config)


admin.site.register(User, UserAdmin)