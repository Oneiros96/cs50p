import sys

def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
        sys.exit()


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        percentage = round((x / y) * 100)
        return(percentage)
    except (ValueError, ZeroDivisionError):
        raise



def gauge(percentage):
    if percentage <= 1:
        return("E")
    if percentage >= 99:
        return("F")
    return(f"{percentage}%")


if __name__ == "__main__":
    main()