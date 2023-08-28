def main():
    output = ommit_vowels(input("Input: "))
    print(output)


def ommit_vowels(input):
    vowels = ("a", "e", "i", "o", "u")
    output = ""

    for letter in input:
        if letter.lower() not in vowels:
            output += letter

    return(output)

if __name__ == "__main__":
    main()