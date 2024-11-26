from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'is_employee', 'is_active', 'is_staff')
    list_filter = ('is_employee', 'is_active', 'is_staff')
    search_fields = ('email', 'full_name', 'personal_number')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'personal_number', 'birth_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_employee', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name', 'personal_number', 'birth_date', 'is_employee'),
        }),
    )

    @admin.action(description='Make selected users staff members')
    def make_staff(self, request, queryset):
        queryset.update(is_staff=True)

    actions = [make_staff]

admin.site.register(CustomUser, CustomUserAdmin)
