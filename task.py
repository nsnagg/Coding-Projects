def is_leap_year(year):
    """ Takes a year, (ie. 1900) and determine if it is a leap year.
        For example, year 2400 is a leap year.
    """
    # Write your code here.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

    return False


# Don't change the function name.

output = int(input("Type year: "))
print(is_leap_year(output))