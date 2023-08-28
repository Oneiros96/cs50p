import sys
import os
import csv
from tabulate import tabulate

def main():
    file_path = check_path(sys.argv)
    table = generate_table(file_path)
    print(table)

def generate_table(file_path):
    with open(file_path) as file:
        csv_data = list(csv.reader(file))
    table = tabulate(csv_data, headers="firstrow", tablefmt="grid")
    return table

def check_path(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = argv[1]

    if not file_path[-4:] == ".csv":
        sys.exit("Not a CSV file")
    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    return(file_path)

if __name__ == "__main__":
    main()