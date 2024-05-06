import re
from datetime import datetime
from enum import StrEnum


class TypeValueEnum(StrEnum):
    PHONE = 'phone'
    EMAIL = 'email'
    DATE = 'date'
    MESSAGE = 'message'


class ValidationService:
    def __init__(self, data: dict) -> None:
        self.data = data

    def validation_func(self, value: str) -> str:
        validation_functions = {
            TypeValueEnum.PHONE: self.phone_validate,
            TypeValueEnum.EMAIL: self.email_validate,
            TypeValueEnum.DATE: self.date_validate
        }
        for field_type, validation_func in validation_functions.items():
            if validation_func(value):
                return field_type
        return TypeValueEnum.MESSAGE


    def phone_validate(self, phone: str) -> bool:
        if not re.match(r'^(\+7|\+8)(\d{3})(\d{3})(\d{2})(\d{2})$', phone):
            return False
        return True

    def email_validate(self, email: str) -> bool:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not bool(re.match(pattern, email)):
            return False
        return True

    def date_validate(self, date: str) -> bool:
        format1 = "%d.%m.%Y"
        format2 = "%Y-%m-%d"
        try:
            if date.count('.'):
                return bool(datetime.strptime(date, format1))
            return bool(datetime.strptime(date, format2))
        except ValueError:
            return False

    def determine_field_types(self) -> dict:
        return {
            key: self.validation_func(value)
            for key, value in self.data.items()
        }
