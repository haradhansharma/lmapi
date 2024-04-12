from django.contrib import admin
from .models import License
import uuid


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['order_ref', 'expiry_date', 'is_valid_lifetime', 'is_banned', 'activation_date', 'license_key']
    readonly_fields = ['license_key']

    def save_model(self, request, obj, form, change):
        if not obj.license_key:
            obj.license_key = str(uuid.uuid4().hex)
        super().save_model(request, obj, form, change)