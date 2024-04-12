from rest_framework import generics, permissions, status
from .models import License
from .serializers import LicenseSerializer, LicenseActivationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.throttling import UserRateThrottle
from django.utils import timezone

class APIHome(APIView):
    def get(self, request, format=None):
        """
        Welcome to License API.

        This API allows you to manage licenses.
        """
        data = {
            "message": "Welcome to License API.",
            "endpoints": {
                "License Detail": reverse("license-detail", kwargs={"license_key": "xxx-key"}, request=request, format=format),
                "Activate License": reverse("license-activate", kwargs={"license_key": "xxx-key", "encrypted_config" : "zxsEdfrSSWWvfd-encrypted-machine-data"}, request=request, format=format)
                # Add more endpoints here if needed
            }
        }
        return Response(data, status=status.HTTP_200_OK)
    
class ObtainAuthTokenView(ObtainAuthToken):    
    @swagger_auto_schema(
        security=[{"Basic": []}],
        operation_description="Get Operation Token",
        responses={
            200: openapi.Response(
                description="Authentication successful",
                examples={
                    'application/json': {
                        "token": "YourAuthTokenHere"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        "detail": "This account is banned. Please contact support."
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if user.is_banned:
            return Response({'detail': 'This account is banned. Please contact support.'}, status=400)
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key})
    
    
class LicenseDetailView(generics.RetrieveAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'license_key'
        
    @swagger_auto_schema(
        operation_summary="Retrieve License Details",
        operation_description="Retrieve details of a license by its license key.",   
        security=[{"Token": []}],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)  
    
class LicenseActivationView(APIView):
    @swagger_auto_schema(
        operation_summary="Activate License",
        operation_description="Update the MAC address associated with a license.",
        request_body=LicenseActivationSerializer,
        responses={
            200: openapi.Response(
                description="Successful activation",
                schema=LicenseSerializer
            ),
            404: "License not found",
            400: "Bad request"
        },
    )
    def patch(self, request, license_key):
        try:
            instance = License.objects.get(license_key=license_key)
        except License.DoesNotExist:
            return Response({"error": "License not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LicenseActivationSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(activation_date=timezone.now())
            return Response(LicenseSerializer(instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
