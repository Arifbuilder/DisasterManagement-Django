from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to show in admin edit page
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {
            "fields": ("phone_number", "latitude", "longitude"),
        }),
    )

    # Fields to show when creating user in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {
            "fields": ("phone_number", "latitude", "longitude"),
        }),
    )

    # Columns in user list page
    list_display = ("username", "email", "phone_number", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)