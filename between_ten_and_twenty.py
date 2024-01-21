class GreaterThanTwentyException(Exception):
    """Exception raised for errors in the input value being greater than 20."""

    def __init__(self, value):
        self.value = value
        self.message = (
            f"{self.__class__.__name__}: The input value {value} is greater than 20."
        )
        super().__init__(self.message)


class LessThanTenException(Exception):
    """Exception raised for errors in the input value being less than 10."""

    def __init__(self, value):
        self.value = value
        self.message = (
            f"{self.__class__.__name__}: The input value {value} is less than 10."
        )
        super().__init__(self.message)


def check_value_between_10_20(value):
    if value > 20:
        raise GreaterThanTwentyException(value)
    elif value < 10:
        raise LessThanTenException(value)
    else:
        return f"The input value {value} is between 10 and 20."


# Example usage
try:
    print("check_value_between_10_20(25): ", check_value_between_10_20(25))
except Exception as e:
    print(e)


try:
    print("check_value_between_10_20(5): ", check_value_between_10_20(5))
except Exception as e:
    print(e)

try:
    print("check_value_between_10_20(15): ", check_value_between_10_20(15))
except Exception as e:
    print(e)
