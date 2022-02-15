from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
# decorator : 바로 밑 클래스에 models.User을 입력해주는 역할.
# == admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
