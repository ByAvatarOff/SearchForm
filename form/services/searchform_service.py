from services.validation_service import phone_validate, email_validate, date_validate
from searchform.models import TinyDbManager


#  TODO its a shit need remake
def form_doesnt_exist(data_request: dict) -> dict:
    """

    """
    response = {}
    for data in data_request.keys():
        if date_validate(data_request[data]):
            response[data] = 'date'
        elif phone_validate(data_request[data]):
            response[data] = 'phone'
        elif email_validate(data_request[data]):
            response[data] = 'email'
        else:
            response[data] = 'text'
    return response


def check_field_type(record: dict, data_request: dict) -> bool:
    """
    Func for check field type
    if request value type and value type on template form same
    return True
    else return False
    """
    dict_values_type = form_doesnt_exist(data_request)
    if set(dict_values_type.values()).issubset(set(record.values())):
        return True
    return False


def filter_forms(data_request: dict) -> str:
    """
    Func for filter forms
    if name and type fields are same return template form name
    else return empty string
    """
    db = TinyDbManager().db
    for record in db.all():
        if (data_request and
                set(data_request.keys()).issubset(set(record.keys())) and
                check_field_type(record, data_request)):
            return record.get('name')
    return ''
