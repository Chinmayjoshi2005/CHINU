from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),
    # Add other app URLs here as needed
]