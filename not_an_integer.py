from math import pi


class NotAnIntegerException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = (
            f"{self.__class__.__name__}: The input value {value} is not an integer."
        )
        super().__init__(self.message)


def check_value_is_integer(value):
    if not isinstance(value, int):
        raise NotAnIntegerException(value)
    else:
        return f"The input value {value} is an integer."


# Example usage
try:
    print("check_value_is_integer(25): ", check_value_is_integer(25))
except Exception as e:
    print(e)

try:
    print("check_value_is_integer(5): ", check_value_is_integer(5))
except Exception as e:
    print(e)

try:
    print("check_value_is_integer(pi): ", check_value_is_integer(pi))
except Exception as e:
    print(e)
