import sys
import os

def main():
    file_path = check_path(sys.argv)
    print(count_lines(file_path))

def check_path(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = argv[1]

    if not file_path[-3:] == ".py":
        sys.exit("Not a Python file")
    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    return(file_path)

def count_lines(file_path):
    line_count = 0
    with open(file_path, "r") as file:
        for line in file:
            if line.lstrip().startswith("#"):
                continue
            elif line.isspace():
                continue
            else:
                line_count += 1
    return(line_count)

if __name__ == "__main__":
    main()