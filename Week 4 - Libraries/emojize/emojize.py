import emoji

def main():
    print("Output:", emoji.emojize(input("Input: "), language="alias"))

if __name__ == "__main__":
    main()