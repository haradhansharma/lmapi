from django.db import models

class License(models.Model):
    order_ref = models.CharField(max_length=100)
    email = models.EmailField()
    license_key = models.CharField(max_length=100, unique=True, help_text="License data. Required when updating a license.", editable=False)
    expiry_date = models.DateField(null=True, blank=True)
    is_valid_lifetime = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    activation_date = models.DateTimeField(null=True, blank=True)
    encrypted_config = models.TextField(null=True, blank=True, help_text="Encrypted configuration data. Required when updating a license.")
    