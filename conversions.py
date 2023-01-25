def bool_to_binary_char(boolean: bool) -> str:
    """Converts a boolean to a binary string ("0" or "1")"""
    return str(int(boolean))


def binary_char_to_bool(char: str) -> bool:
    """Converts a binary string to a boolean"""
    return bool(int(char))
