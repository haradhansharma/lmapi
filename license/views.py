from rest_framework import generics, permissions, status
from .models import License
from .serializers import LicenseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authtoken.views import ObtainAuthToken

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
    @swagger_auto_schema(security=[{"Basic": []}])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class LicenseDetailView(generics.RetrieveAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'license_key'
    
    
    @swagger_auto_schema(
        operation_description="Get a license Information",        
        security=[{"Token": []}],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class LicenseActivationView(generics.UpdateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = [permissions.IsAuthenticated] 
    lookup_field = 'license_key'
    http_method_names = ['put']
    
    @swagger_auto_schema(
        operation_description="Activate a license",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['encrypted_config'],
            properties={
                'encrypted_config': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={
            200: openapi.Response(
                description="License activated successfully",
                examples={
                    'application/json': {
                        "message": "License activated successfully"
                    },
                    'text/plain': """
                        {
                            "message": "License activated successfully"
                        }
                    """
                }
            ),
            400: "Bad request",
            401: "Unauthorized"
        },
        security=[{"Token": []}],

    )

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    