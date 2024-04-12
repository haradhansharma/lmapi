from django.contrib import admin

from common.models import Contact, Software

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'file', 'created_at', 'updated_at']
    # readonly_fields = ['license_key', 'activation_date', 'mac_address']
    
@admin.register(Contact)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
