def is_valid_imei(value: str) -> str:
    if len(value) not in range(15, 17):
        raise ValueError(f'{value} wrong length of imei')
    if not value.isdigit():
        raise ValueError(f'{value} imei must contain only nums')
    return value
