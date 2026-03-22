# Task 1: Check if number is even or odd

try:
    num = int(input("Enter an integer number: "))

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

except ValueError:
    print("Invalid input! Please enter an integer.")