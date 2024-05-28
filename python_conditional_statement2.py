# Question 2: The Greatest Showdown

# Task 1: Identify the Greatest

first_number = int(input("You will be asked for three whole numbers. Please enter your first whole number: "))
second_number = int(input("Please enter your second whole number: "))
third_number = int(input("Please enter your third whole number: "))

if first_number >= second_number and first_number >= third_number:
    print(f"The largest number is {first_number}.")
elif second_number >= first_number and second_number >= third_number:
    print(f"The largest number is {second_number}.")
elif third_number >= first_number and third_number >= second_number:
    print(f"The largest number is {third_number}.")

# Task 2: Identify the Smallest

if first_number <= second_number and first_number <= third_number:
    print(f"The smallest number is {first_number}.")
elif second_number <= first_number and second_number <= third_number:
    print(f"The smallest number is {second_number}.")
elif third_number <= first_number and third_number <= second_number:
    print(f"The smallest number is {third_number}.")

# Task 3: Equality Check

if first_number > second_number and first_number > third_number and second_number < third_number:
    print(f"The largest number is the first number, {first_number}, and the smallest number is the second number, {second_number}.")
elif first_number == second_number and third_number < first_number:
    print(f"The first two numbers are equal, {first_number}, and the smallest number is the third number, {third_number}.")
elif first_number == second_number and third_number > first_number:
    print(f"The first two numbers are equal, {first_number}, and the largest number is the third number, {third_number}.")

elif first_number > second_number and first_number > third_number and third_number < second_number:
    print(f"The largest number is the first number, {first_number}, and the smallest number is the third number, {third_number}.")
elif first_number == third_number and second_number < first_number:
    print(f"The first and third numbers are equal, {first_number}, and the smallest number is the second number, {second_number}.")
elif first_number == third_number and second_number > first_number:
    print(f"The first and third numbers are equal, {first_number}, and the largest number is the second number, {second_number}.")

elif second_number > first_number and second_number > third_number and first_number < third_number:
    print(f"The largest number is the second number, {second_number}, and the smallest number is the first number, {first_number}.")
elif second_number == third_number and first_number < second_number:
    print(f"The second and third numbers are equal, {second_number}, and the smallest number is the first number, {first_number}.")
elif second_number == third_number and first_number > second_number:
    print(f"The second and third numbers are equal, {second_number}, and the largest number is the first number, {first_number}.")

elif second_number > first_number and second_number > third_number and third_number < first_number:
    print(f"The largest number is the second number, {second_number}, and the smallest number is the third number, {third_number}.")
elif third_number > first_number and third_number > second_number and first_number < second_number:
    print(f"The largest number is the third number, {third_number}, and the smallest number is the first number, {first_number}.")
elif third_number > first_number and third_number > second_number and first_number > second_number:
    print(f"The largest number is the third number, {third_number}, and the smallest number is the second number, {second_number}.")
else:
    print(f"All three numbers are equal, {first_number}! 😎")