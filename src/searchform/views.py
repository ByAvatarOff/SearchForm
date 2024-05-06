from rest_framework import viewsets, status
from rest_framework.response import Response
from searchform.services import ValidationService, FormService


class FormViewSet(viewsets.ViewSet):

    def get_name_form(self, request) -> Response:
        validate_service = ValidationService(request.data)
        validate_data = validate_service.determine_field_types()

        form_service = FormService()
        data = form_service.get_form_from_mongo(validate_data=validate_data)

        return Response(status=status.HTTP_200_OK, data=data)
