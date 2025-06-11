from django.contrib import admin
from .models import Guard, Service, User, Contact

class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_staff', 'is_active')

class AdminGuard(admin.ModelAdmin):
    list_display = ('name', 'experience', 'availability_status')
    search_fields = ('name',)
    list_filter = ('availability_status',)

class AdminService(admin.ModelAdmin):
    list_display = ('service_name',)
    search_fields = ('service_name',)

class AdminContact(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('created_at',)

admin.site.register(User, AdminUser)
admin.site.register(Guard, AdminGuard)
admin.site.register(Service, AdminService)
admin.site.register(Contact, AdminContact)
