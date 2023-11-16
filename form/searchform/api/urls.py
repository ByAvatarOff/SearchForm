from django.urls import path
from searchform.api.views import FormViewSet

urlpatterns = [
    path('', FormViewSet.as_view({"post": "get_name_form"}),
         name='get_name_form'
),
]
