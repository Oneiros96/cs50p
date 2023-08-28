def main():
    user_input = input("Expression: ").split(" ")
    x = int(user_input[0])
    y = int(user_input[2])
    match user_input[1]:
        case "+":
            print(float(x + y))
        case "-":
            print(float(x - y))
        case "*":
            print(float(x * y))
        case "/":
            print(float(x / y))

main()