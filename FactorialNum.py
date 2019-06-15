""" Write a recursive function to print the factorial of a number from user."""

def factorial(number):                      #function for factorial
    if number==0:
        return 1
    else:
        return number*factorial(number-1)

number=int(input("Enter a number to find factorial for: "))
print("Factorial of number is ", factorial(number))
