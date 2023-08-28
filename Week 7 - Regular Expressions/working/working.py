import re
import sys

def main():
    print(convert(input("Hours: ")))
    sys.exit()

def convert(s):
    blocks = re.search(r"^(\d+|\d+:\d+) (PM|AM) to (\d+|\d+:\d+) (PM|AM)$", s)
    if not blocks:
        raise ValueError
    time_1 = [blocks.group(1), blocks.group(2)]
    time_2 = [blocks.group(3), blocks.group(4)]
    time_1, time_2 = to_24h(time_1), to_24h(time_2)
    return(f"{time_1} to {time_2}")

def to_24h(time):
    if ":" in time[0]:
        hour, minutes = map(int, time[0].split(":"))
    else:
        hour, minutes = int(time[0]), 0

    if hour > 12 or minutes > 59:
            raise ValueError

    if time[1] == "AM" and hour == 12:
        hour = 0
    if time[1] == "PM":
        hour = int(hour) + 12
        if hour == 24:
            hour = 12


    return(f"{hour:02d}:{minutes:02d}")

if __name__ == "__main__":
    main()