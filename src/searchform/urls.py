from django.urls import path

from searchform.views import FormViewSet

urlpatterns = [
    path('', FormViewSet.as_view({"post": "get_name_form"}),
         name='form-view'
),
]
