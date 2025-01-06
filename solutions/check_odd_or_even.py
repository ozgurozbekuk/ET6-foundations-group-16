def check_odd_or_even(num):
    assert isinstance(num, int), "num must be an integer"
    return "Even" if num % 2 == 0 else "Odd"
