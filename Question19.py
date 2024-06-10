# Input a string from the user
input_string = input("Enter a string: ")

# List of punctuation characters to remove
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Initialize an empty string to store the result
result_string = ""

# Iterate over each character in the input string
for char in input_string:
    if char not in punctuation:
        result_string += char

# Print the string without punctuation
print("String without punctuation:", result_string)
