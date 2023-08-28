import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # between 2 and 6 chars
    if not 2 <= len(s) <= 6:
        return False
    # starts with 2 letters
    if not isinstance(s[0], str) or not isinstance(s[1], str):
        return False
    # numbers at the end, first number cant be 0
    pattern = r"^[A-Za-z]+[1-9][0-9]*$|^[A-Za-z]+$"
    if not re.match(pattern, s):
        return False
    # no periods spaces or points
    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()