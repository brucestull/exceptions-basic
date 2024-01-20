class GreaterThanTwentyError(Exception):
    """Exception raised for errors in the input value being greater than 20."""
    def __init__(self, value):
        self.value = value
        self.message = f"The value {value} is greater than 20."
        super().__init__(self.message)

class LessThanTenError(Exception):
    """Exception raised for errors in the input value being less than 10."""
    def __init__(self, value):
        self.value = value
        self.message = f"The value {value} is less than 10."
        super().__init__(self.message)

def check_value(value):
    if value > 20:
        raise GreaterThanTwentyError(value)
    elif value < 10:
        raise LessThanTenError(value)
    else:
        return "Value is between 10 and 20."

# Example usage
try:
    print(check_value(25))
except Exception as e:
    print(e)

try:
    print(check_value(5))
except Exception as e:
    print(e)

try:
    print(check_value(15))
except Exception as e:
    print(e)
