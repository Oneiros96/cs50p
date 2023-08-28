import sys
import csv
import os

def main():
    in_file, out_file = check_args(sys.argv)
    out_content = get_out_content(in_file)
    write_outfile(out_file, out_content)
    sys.exit()

def write_outfile(out_file, out_content):
    with open(out_file, "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in out_content:
            writer.writerow(row)




def get_out_content(in_file):
    out_content = []
    with open(in_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            dict = {
                "first": first,
                "last": last,
                "house": row["house"]
            }
            out_content.append(dict)
    return(out_content)



def check_args(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")

    in_file = argv[1]
    out_file = argv[2]

    if not in_file[-4:] == ".csv" or not os.path.exists(in_file):
        sys.exit(f"Could not read {argv[1]}")

    return(in_file, out_file)

if __name__ == "__main__":
    main()