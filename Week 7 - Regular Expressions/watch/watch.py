import re
import sys


def main():
    print(parse(input("HTML: ")))
    sys.exit()


def parse(s):
    video = re.search(r'iframe.+youtube\.com/embed/([^"]+)', s)
    if video:
        return(f"https://youtu.be/{video.group(1)}")
    else:
        return(None)


if __name__ == "__main__":
    main()