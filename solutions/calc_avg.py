def calculate_average(numbers):
    """
    Calculates the average of a list of numbers (integers or floats).
    Returns:
    - float: Average of the numbers.
    - None: If the list is empty.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
