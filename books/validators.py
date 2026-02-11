import re

from django.core.exceptions import ValidationError


def validate_isbn(value):

    clean_value = re.sub(r'[- ]', '', value)

    if not re.match(r'^(\d{10}|\d{13})$', clean_value):
        raise ValidationError('Enter a valid 10 or 13-digit ISBN.')
