from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/form/', include('searchform.urls')),
    path('admin/', admin.site.urls),
]
