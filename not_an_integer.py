from math import pi


class NotAnIntegerException(Exception):
    def __init__(self, value):
        self.value = value
        self.message = (
            f"{self.__class__.__name__}: The input value, {value}, is not an integer."
        )
        super().__init__(self.message)


def check_value_is_integer(value):
    if not isinstance(value, int):
        raise NotAnIntegerException(value)
    else:
        return f"The input value, {value}, is an integer."


# Example usage
TWENTY_FIVE = 25
FIVE = 5
PI = pi
try:
    print("check_value_is_integer(TWENTY_FIVE): ", check_value_is_integer(TWENTY_FIVE))
except Exception as e:
    print(e)

try:
    print("check_value_is_integer(FIVE): ", check_value_is_integer(FIVE))
except Exception as e:
    print(e)

try:
    print("check_value_is_integer(PI): ", check_value_is_integer(PI))
except Exception as e:
    print("\nAttempted to run check_value_is_integer(PI) and got an exception:")
    print(e)
