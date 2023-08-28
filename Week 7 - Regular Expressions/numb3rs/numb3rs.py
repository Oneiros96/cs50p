import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    blocks = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    try:
        for i in range(1, 5):
            block = int(blocks.group(i))
            if 0 <= block and block <= 255:
                continue
            else:
                return False

    except AttributeError:
        return False

    return True

if __name__ == "__main__":
    main()