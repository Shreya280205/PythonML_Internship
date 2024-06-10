if __name__ == "__main__":
    # Input the first number
    num1 = float(input("Enter the first number: "))

    # Input the operator
    operator = input("Enter the operator (+, -, *, /): ")

    # Input the second number
    num2 = float(input("Enter the second number: "))

    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            exit()
    else:
        print("Invalid operator")
        exit()

    # Print the result
    print("Result:", result)
