def main():
    while True:
        x, y = get_ints()

        if x == 0 and y == 0:
            print("E")
            return

        # restart loop if tests for input validation fail
        if not test_ints(x, y):
            continue

        result = get_result(x, y)



        print(result)
        return



def get_ints():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            return (x, y)
        except ValueError:
            pass

def test_ints(x, y):
    if y == 0:
        return False
    if x > y:
        return False
    return True

def get_result(x, y):
    result = round((x / y) * 100)
    if result <= 1:
        return("E")
    if result >= 99:
        return("F")
    return(f"{result}%")

if __name__ == "__main__":
    main()
