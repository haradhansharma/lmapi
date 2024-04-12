

from django.urls import path
from .views import contact_view, download_software, downloads, home, success_view


app_name = 'common'
urlpatterns = [
    path('', home, name="home"), 
    path('downloads/', downloads, name='downloads'),       
    path('download/<uuid:file_id>/', download_software, name='download_software'),   
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    
]