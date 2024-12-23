from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rps_api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('scoreboard/', include('rps_api.urls')), 
    path('', include('rps_api.urls')),
]
