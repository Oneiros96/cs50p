def main():
    word = shorten(input("Input: "))
    print(word)


def shorten(input):
    vowels = ("a", "e", "i", "o", "u")
    output = ""

    for letter in input:
        if letter.lower() not in vowels:
            output += letter

    return(output)

if __name__ == "__main__":
    main()