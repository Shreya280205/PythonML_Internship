# Input a list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into individual number strings and convert them to integers
number_list = [float(num) for num in numbers.split()]

# Calculate the sum of the numbers
total_sum = sum(number_list)

# Print the sum
print("The sum of the numbers is:", total_sum)
