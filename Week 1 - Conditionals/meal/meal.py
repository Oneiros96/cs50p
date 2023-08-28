def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    # conversion normal minutes(60 per hour) to industry minutes(100 per hour) to get a propper float
    minutes = (int(minutes) * 100) / 60
    time = int(hours) + (minutes / 100)
    return(time)


if __name__ == "__main__":
    main()