from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):  # type: ignore[type-arg]
    class Meta:
        model = CustomUser
        # django-stubs doesn't like `UserCreationForm.Meta.fields + ("name",)`
        # since it doesn't see `Meta`; define our own `Meta`.
        fields = ("username", "password1", "password2", "name")


class CustomUserChangeForm(UserChangeForm):  # type: ignore[type-arg]
    class Meta:
        model = CustomUser
        fields = ("username", "email", "name", "is_active", "is_staff")
