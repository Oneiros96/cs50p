import inflect
p = inflect.engine()

def main():
    names = get_names()
    output = get_output(names)
    print(output)

def get_names():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            return(names)

def get_output(names):
    names = p.join(names)
    return(f"Adieu, adieu, to {names}")



if __name__ == "__main__":
    main()