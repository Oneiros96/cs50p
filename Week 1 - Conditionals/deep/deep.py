CORRECT_ANSWERS = ("42", "forty two", "forty-two")

def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip(" ")
    if user_input in CORRECT_ANSWERS:
        print("Yes")
    else:
        print("No")


main()