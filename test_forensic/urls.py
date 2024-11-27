from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_snort.urls')),
    path('test-xss/', include('test_xss.urls')),
]
