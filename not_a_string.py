class NotAStringException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = (
            f"{self.__class__.__name__}: The input value, {value}, is not a string."
        )
        super().__init__(self.message)


def check_value_is_string(value):
    if not isinstance(value, str):
        raise NotAStringException(value)
    else:
        return f"The input value, {value}, is a string."


# Example usage
HELLO = "Hello"
FIVE = 5
try:
    print("check_value_is_string(HELLO): ", check_value_is_string(HELLO))
except Exception as e:
    print(e)

try:
    print("check_value_is_string(FIVE): ", check_value_is_string(FIVE))
except Exception as e:
    print(e)
