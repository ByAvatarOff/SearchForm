from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/form/', include('searchform.api.urls')),
    path('admin/', admin.site.urls),
]
