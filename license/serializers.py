
from rest_framework import serializers
from .models import License, Record
from django.utils import timezone
    
    
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['order_ref', 'license_key', 'expiry_date', 'is_valid_lifetime', 'is_banned', 'activation_date', 'mac_address', 'ids']
        read_only_fields = ['license_key', 'expiry_date', 'is_valid_lifetime', 'is_banned', 'activation_date']  # Fields that should be read-only

    def validate(self, attrs):
        license_key = attrs.get('license_key')
        if license_key is None:
            raise serializers.ValidationError("License key is required.")
        return attrs

class LicenseActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['mac_address', 'ids']

    def validate(self, attrs):     
        mac_address = attrs.get('mac_address')        
        if not mac_address:
            raise serializers.ValidationError("MAC address is required.")  
        
        ids = attrs.get('ids')        
        if not ids:
            raise serializers.ValidationError("Ids is required.")  
        
        # License can be register multiple time for the same machine.      
        if self.instance.mac_address is not None:
            if str(self.instance.mac_address) != str(mac_address):
                raise serializers.ValidationError("This license is not for the machine you wanted to register.")
        
        return attrs
    
class RecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Record
        fields = ['license', 'pw']
        

        
    
