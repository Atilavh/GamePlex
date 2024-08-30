from django.contrib import admin
from . import models


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'is_active', 'is_superuser', 'is_staff')


admin.site.register(models.User, UserAdmin)
