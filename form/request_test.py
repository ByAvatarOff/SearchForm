import requests


url = 'http://127.0.0.1:8001/api/form/'


def get_name_form_success():
    """
    Form was found in db
    """
    response = requests.post(url, {
        "user_email": "tsp7439@gmail.com",
        "user_phone": "+78822233333",
        "user_date": "2022-12-1"
         })
    assert response.status_code == 200
    assert response.json() == "User Form"
    print('test get_name_form_success OK')


def not_correct_type_key():
    """
    Data keys not found in db
    return json obj with fields type
    """
    response = requests.post(url, {
        "my_email": "tsp7439@gmail.com",
        "my_phone": "+78822233333",
    })
    assert response.status_code == 200
    assert response.json() == {
        "my_email": 'email',
        'my_phone': 'phone'
    }
    print('test not_correct_type_key OK')


def not_validate_value():
    """
    type of values not validate
    return json obj with fields type
    """
    response = requests.post(url, {
        "add_date": "11.13.2020",
        "phone": "+7882223",
        "email": 'new@'
    })
    assert response.status_code == 200
    assert response.json() == {
        "add_date": 'text',
        'phone': 'text',
        'email': 'text'
    }
    print('test not_correct_type_value OK')


get_name_form_success()
not_correct_type_key()
not_validate_value()