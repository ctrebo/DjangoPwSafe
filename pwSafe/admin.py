from django.contrib import admin

from .models import Password
# Register your models here.


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    fieldsets = (
        ("Informations", {
            "fields":("title", "website", "username", "email", "password")
        }),
        ("User", {
            "fields":('user',)
        }),
    )