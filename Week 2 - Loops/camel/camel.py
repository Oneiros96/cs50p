def main():
    output = to_snake_case(input("camelCase: "))
    print(output)

def to_snake_case(user_input):
    output = ""
    for letter in user_input:
        if letter.isupper():
            letter = f"_{letter.lower()}"
        output += letter
    return output

if __name__ == "__main__":
    main()