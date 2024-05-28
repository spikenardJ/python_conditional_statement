# Question 2: Leap Year Explorer

# Task 1: Leap Year Checker

leap_year_checker = int(input("Leap Year Checker. Please enter year here: "))

if leap_year_checker % 4 == 0 and leap_year_checker % 100 != 0:
    print(f"{leap_year_checker} is a leap year!")
elif leap_year_checker % 400 == 0 and leap_year_checker % 100 == 0:
    print(f"{leap_year_checker} is a leap year!")
else:
    print(f"{leap_year_checker} is not a leap year.")