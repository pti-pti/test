"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# تعریف ثوابت (Constants)
# زمان پخت مورد انتظار بر حسب دقیقه (معمولاً در این تمرین ۴۰ دقیقه در نظر گرفته می‌شود)
EXPECTED_BAKE_TIME = 40
# زمان آماده‌سازی برای هر لایه (معمولاً ۲ دقیقه به ازای هر لایه در نظر گرفته می‌شود)
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.

    Returns:
        int: The preparation time (in minutes) based on 'PREPARATION_TIME'.

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed cooking time (preparation + baking) in minutes.

    Function that returns the total number of minutes you've been cooking,
    summing the preparation time and the time the lasagna has spent in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time