# Input a list of numbers from the user
numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into individual number strings and convert them to integers
number_list = [int(num) for num in numbers.split()]

# Find the minimum and maximum values in the list
min_value = min(number_list)
max_value = max(number_list)

# Print the minimum and maximum values
print("The minimum value in the list is:", min_value)
print("The maximum value in the list is:", max_value)
