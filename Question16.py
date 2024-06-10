def count_character_frequency(input_string):
    # Create an empty dictionary to store the frequency of each character
    frequency_dict = {}

    # Iterate over each character in the string
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict


if __name__ == "__main__":
    # Input string from the user
    input_string = input("Enter a string: ")

    # Get the character frequency dictionary
    frequency_dict = count_character_frequency(input_string)

    # Print the frequency of each character
    for char, frequency in frequency_dict.items():
        print(f"'{char}': {frequency}")
