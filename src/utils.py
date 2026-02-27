def _validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers (int or float).")

def add(a, b):
    _validate_numbers(a, b)
    return a + b

def subtract(a, b):
    _validate_numbers(a, b)
    return a - b

def multiply(a, b):
    _validate_numbers(a, b)
    return a * b