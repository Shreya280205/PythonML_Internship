# Input a list of elements from the user
elements = input("Enter a list of elements separated by spaces: ")

# Split the input string into individual elements
element_list = elements.split()

# Input the element to count occurrences of
target_element = input("Enter the element to count occurrences of: ")

# Count the occurrences of the target element in the list
occurrences = element_list.count(target_element)

# Print the number of occurrences
print(f"The element '{target_element}' occurs {occurrences} times in the list.")
