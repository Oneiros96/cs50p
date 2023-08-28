import validators

def main():
    result = validators.email(input("What's your email address? "))
    if result != True:
        print("Invalid")
    else:
        print("Valid")

if __name__ == "__main__":
    main()