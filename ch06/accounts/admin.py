from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):  # type: ignore[type-arg]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "name", "is_staff"]
    fieldsets = (
        *(UserAdmin.fieldsets or ()),  # if None, use empty tuple
        (None, {"fields": ("name",)}),
    )

    add_fieldsets = (
        *(UserAdmin.add_fieldsets or ()),
        (None, {"fields": ("name",)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
