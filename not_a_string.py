class NotAStringException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = (
            f"{self.__class__.__name__}: The input value {value} is not a string."
        )
        super().__init__(self.message)


def check_value_is_string(value):
    if not isinstance(value, str):
        raise NotAStringException(value)
    else:
        return f"The input value {value} is a string."


# Example usage
try:
    print("check_value_is_string('Hello'): ", check_value_is_string("Hello"))
except Exception as e:
    print(e)

try:
    print("check_value_is_string(5): ", check_value_is_string(5))
except Exception as e:
    print(e)
