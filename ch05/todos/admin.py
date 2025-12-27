from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "title",
        "body",
    )


admin.site.register(Todo, TodoAdmin)
