user_input=input("Please enter a string: ")

with open("C:/Users/ShreyaKaushik/OneDrive/Desktop/New folder/Text.txt","w") as file:
    file.write(user_input)

print(f"{user_input} has been written to text file.")