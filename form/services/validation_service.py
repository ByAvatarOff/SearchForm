import re
from datetime import datetime


def phone_validate(phone: str) -> bool:
    """
    Func for validate phone use regular expression
    """
    if not re.match(r'^(\+7|\+8)(\d{3})(\d{3})(\d{2})(\d{2})$', phone):
        return False
    return True


def email_validate(email: str) -> bool:
    """
    Func for validate email use regular expression
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not bool(re.match(pattern, email)):
        return False
    return True


def date_validate(date: str) -> bool:
    """
    Func for validate date on two formats use base python module datetime
    """
    format1 = "%d.%m.%Y"
    format2 = "%Y-%m-%d"
    try:
        if date.count('.'):
            return bool(datetime.strptime(date, format1))
        return bool(datetime.strptime(date, format2))
    except ValueError:
        return False