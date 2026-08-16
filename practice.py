def is_leap_year(year: int) -> bool:
    """
    Checks whether a given year is a leap year based on standard Gregorian calendar rules:
    - A year divisible by 400 is a leap year.
    - A year divisible by 100 but not 400 is not a leap year.
    - A year divisible by 4 but not 100 is a leap year.
    - Other years are not leap years.
    
    :param year: The year as an integer
    :return: True if year is a leap year, False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    print("=== Leap Year Checking Logic Demo ===")
    
    test_years = [
        (2000, True, "Divisible by 400"),
        (2400, True, "Divisible by 400"),
        (1600, True, "Divisible by 400"),
        (1900, False, "Divisible by 100, but not 400"),
        (2100, False, "Divisible by 100, but not 400"),
        (1800, False, "Divisible by 100, but not 400"),
        (2024, True, "Divisible by 4, but not 100"),
        (2004, True, "Divisible by 4, but not 100"),
        (2020, True, "Divisible by 4, but not 100"),
        (2023, False, "Not divisible by 4"),
        (2025, False, "Not divisible by 4"),
        (2019, False, "Not divisible by 4"),
    ]
    
    print(f"{'Year':<8} | {'Is Leap Year':<12} | {'Expected':<10} | {'Status':<6} | {'Reason'}")
    print("-" * 65)
    
    for year, expected, reason in test_years:
        result = is_leap_year(year)
        status = "PASSED" if result == expected else "FAILED"
        print(f"{year:<8} | {str(result):<12} | {str(expected):<10} | {status:<6} | {reason}")


if __name__ == "__main__":
    main()
