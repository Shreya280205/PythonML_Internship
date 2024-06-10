# Input two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Clean up the strings by removing spaces and converting to lowercase
str1_cleaned = str1.lower()
str2_cleaned = str2.lower()

# Check if the sorted characters of both strings are equal
if sorted(str1_cleaned) == sorted(str2_cleaned):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")
