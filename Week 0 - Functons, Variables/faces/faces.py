def convert(input):
    output = input.replace(":)", "🙂").replace(":(", "🙁")
    return(output)

def main():
    user_input = input("Input:")
    output = convert(user_input)
    print(output)

main()