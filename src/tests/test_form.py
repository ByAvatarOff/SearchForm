from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TestForm:
    base_url = reverse("form-view")

    def test_get_name_template_success(self, client: APIClient, valid_data: dict) -> None:
        response = client.post(self.base_url, valid_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == "User Form"

    def test_over_field_in_form(self, client: APIClient, over_valid_data: dict) -> None:
        response = client.post(self.base_url, over_valid_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == "User Form"

    def test_not_correct_type_key_failed(self, client: APIClient, not_match_data: dict) -> None:
        response = client.post(self.base_url, not_match_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "my_email": 'email',
            'my_phone': 'phone'
        }

    def test_not_valid_value_failed(self, client: APIClient, invalid_type_data: dict) -> None:
        response = client.post(self.base_url, invalid_type_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "add_date": 'message',
            'phone': 'message',
            'email': 'message'
        }
