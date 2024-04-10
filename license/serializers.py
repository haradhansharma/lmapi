
from rest_framework import serializers
from .models import License
from django.utils import timezone

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

    def validate(self, data):  
        if self.instance and 'encrypted_config' in data:         
            if not data.get('encrypted_config'):
                raise serializers.ValidationError("Encrypted config is required.")
            if self.instance.activation_date:
                raise serializers.ValidationError("License is already activated.")
        return data
    
    def update(self, instance, validated_data):        
        instance.activation_date = timezone.now()
        instance.encrypted_config = validated_data.get('encrypted_config', instance.encrypted_config)
        instance.save()
        return instance