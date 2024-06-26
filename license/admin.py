from django.contrib import admin
from .models import License, Record
import uuid


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['order_ref', 'expiry_date', 'mac_address', 'is_valid_lifetime', 'is_banned', 'activation_date', 'license_key']
    readonly_fields = ['license_key', 'activation_date', 'mac_address']

    def save_model(self, request, obj, form, change):
        if not obj.license_key:
            obj.license_key = str(uuid.uuid4().hex)
        super().save_model(request, obj, form, change)
        
        
@admin.register(Record)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['un', 'la']
    readonly_fields = ['un', 'pw', 'la']
        

