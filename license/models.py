import uuid
from django.db import models
from django.urls import reverse

class License(models.Model):
    order_ref = models.CharField(max_length=100)
    license_key = models.CharField(max_length=100, unique=True, help_text="License data. Required when updating a license.", editable=False)
    expiry_date = models.DateField(null=True, blank=True)
    is_valid_lifetime = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    activation_date = models.DateTimeField(null=True, blank=True)
    mac_address = models.CharField(max_length=100, null=True, blank=True)
    ids = models.TextField(null=True, blank=True, help_text='Must be comma separated')
    
    
class Record(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE, related_name='license_ids')
    un = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    la = models.DateTimeField(auto_now=True)
    
    


    