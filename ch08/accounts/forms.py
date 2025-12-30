from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):  # type: ignore[type-arg]
    class Meta:
        model = CustomUser
        fields = ("username", "email")
