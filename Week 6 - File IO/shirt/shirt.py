import sys
from PIL import Image, ImageOps

def main():
    in_file, out_file = check_args(sys.argv)
    create_output(in_file, out_file)
    sys.exit()

def create_output(in_file, out_file):
    shirt = Image.open("shirt.png")
    size = shirt.size

    in_picture = Image.open(in_file)
    in_picture = ImageOps.fit(in_picture, size)
    in_picture.paste(shirt, shirt)
    in_picture.save(out_file)



def check_args(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")

    in_file = argv[1]
    out_file = argv[2]
    file_formats = [".jpg", ".gif", ".png"]
    if in_file[-4:].lower() not in file_formats or out_file[-4:].lower() not in file_formats:
        sys.exit("Invalid input")
    if in_file[-4:].lower() != out_file[-4:].lower():
        sys.exit("Input and output have diffrent extensions")


    return(in_file, out_file)

if __name__ == "__main__":
    main()