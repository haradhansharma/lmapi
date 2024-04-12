
from rest_framework import serializers
from .models import License
from django.utils import timezone

# class LicenseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = License
#         fields = '__all__'

    # def validate(self, data):  
    #     print(data)
    #     if self.instance and 'mac_address' in data:         
    #         if not data.get('mac_address'):
    #             raise serializers.ValidationError("mac address is required.")
    #         if self.instance.activation_date:
    #             raise serializers.ValidationError("License is already activated.")
    #     return data
    
    # def update(self, instance, validated_data):            
    #     instance.activation_date = timezone.now()
    #     instance.mac_address = validated_data.get('mac_address', instance.mac_address)
    #     instance.save()
    #     return instance   
    
    
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['order_ref', 'license_key', 'expiry_date', 'is_valid_lifetime', 'is_banned', 'activation_date', 'mac_address']
        read_only_fields = ['license_key', 'expiry_date', 'is_valid_lifetime', 'is_banned', 'activation_date']  # Fields that should be read-only

    def validate(self, attrs):
        license_key = attrs.get('license_key')
        if license_key is None:
            raise serializers.ValidationError("License key is required.")
        return attrs

class LicenseActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['mac_address']

    def validate(self, attrs):     
        mac_address = attrs.get('mac_address')        
        if not mac_address:
            raise serializers.ValidationError("MAC address is required.")  
        
        # License can be register multiple time for the same machine.      
        if self.instance.mac_address is not None:
            if str(self.instance.mac_address) != str(mac_address):
                raise serializers.ValidationError("This license is not for the machine you wanted to register.")
        
        return attrs
        
    
