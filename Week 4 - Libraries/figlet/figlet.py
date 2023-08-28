from pyfiglet import Figlet
import sys
figlet = Figlet()

def main():
    # no additional arguments sys.argv[0] = script name
    if len(sys.argv) == 1:
        print(figlet.renderText(input("Input: ")))
    # 2 additional arguments of which the first is -f or --fonts
    if len(sys.argv) == 3:
        if not sys.argv[1] == "-f" or sys.argv[1] == "--font":
            sys.exit("Invalid usage")

        font_list = figlet.getFonts()
        if not sys.argv[2] in font_list:
            sys.exit("Invalid usage")

        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Input: ")))

    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()