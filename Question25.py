source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

# Open the source file in read mode and destination file in write mode
try:
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            # Read the content of the source file and write it to the destination file
            destination.write(source.read())
    print("File contents copied successfully.")
except FileNotFoundError:
    print("Error: One or both files not found.")
except Exception as e:
    print("An error occurred:", e)