"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""


class InvalidInput(Exception):
    pass


def no_of_handshakes(no_people):

    try:

        # Make sure it is an integer
        if no_people.is_integer():
            pass
        else:
            raise InvalidInput("Invalid input: Number of people must be an integer.")

        # Make sure it is positive
        if no_people < 0:
            raise InvalidInput("Invalid input: Cannot be a negative number.")

        # Calculate the number of handshakes
        total_handshakes = no_people * (no_people - 1) // 2
        return total_handshakes

    except AttributeError as e:
        print(f"Cannot be a string!: {e}")
        raise

print(no_of_handshakes(20))







