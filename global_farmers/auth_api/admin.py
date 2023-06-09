from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'government_id', 'user_type', 'mobile_number', 'country', 'email', 'location', 'created_at', 'password', 'is_active', 'is_staff')


admin.site.register(User, UserAdmin)
