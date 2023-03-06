import datetime


def date_validator(value):
    if value < datetime.date.today():
        raise ValueError('Date cannot be in the past.')


def validate_load_size(value):
    if 0 > value or value > 15:
        raise ValueError('The value should be between 0 and 15.00 meters')


def validate_load_weight(value):
    if 0 > value or value > 28:
        raise ValueError('The value should be between 0 and 28 tons.')
