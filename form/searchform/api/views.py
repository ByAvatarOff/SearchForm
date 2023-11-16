from rest_framework import viewsets, status
from rest_framework.response import Response
from services.searchform_service import form_doesnt_exist, filter_forms


class FormViewSet(viewsets.ViewSet):

    def get_name_form(self, request) -> Response:
        """
        Endpoint for return name of template form
        if name and type fields are same
        else return a json object with key -> name field and value -> type of field

        example:
        field_name: email
        field_name2: text
        field_name3: phone
        """
        response_forms = filter_forms(request.data)
        if not response_forms:
            data = form_doesnt_exist(request.data)
            return Response(status=status.HTTP_200_OK, data=data)
        return Response(status=status.HTTP_200_OK, data=response_forms)
