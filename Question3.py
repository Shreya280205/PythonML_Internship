def factorial(n):
    # Initializing the result to 1
    result = 1

    # Looping from 1 to n (inclusive) and multiplying the result
    for i in range(1, n +1):
        result *= i
    return result


# Taking input from the user
number = int(input("Enter a number: "))

# Calculating the factorial
fact = factorial(number)

# Printing the result
print(f"The factorial of {number} is {fact}")