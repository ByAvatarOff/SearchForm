import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def valid_data() -> dict:
    return {
        "user_email": "tsp7439@gmail.com",
        "user_phone": "+78822233333",
        "user_date": "2022-12-1",
        "text_message": "test text"
    }


@pytest.fixture
def over_valid_data() -> dict:
    return {
        "user_email": "tsp7439@gmail.com",
        "user_phone": "+78822233333",
        "user_date": "2022-12-1",
        "text_message": "test text",
        "user_birthday": "2002-12-1"
    }


@pytest.fixture
def not_match_data() -> dict:
    return {
        "my_email": "tsp7439@gmail.com",
        "my_phone": "+78822233333",
    }


@pytest.fixture
def invalid_type_data() -> dict:
    return {
        "add_date": "11.13.2020",
        "phone": "+7882223",
        "email": 'new@'
    }
