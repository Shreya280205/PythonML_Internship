import csv

def read_csv_file(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    # Input the path to the CSV file
 file_path = input("Enter the path to the CSV file: ")
 read_csv_file(file_path)
