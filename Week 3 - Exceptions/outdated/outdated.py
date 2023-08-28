MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    year, month, day = get_date()
    print(f"{year:04}-{month:02}-{day:02}")


def get_date():
    while True:
        try:
            date = input("Date:")
            # for MM/DD/YYYY formated input
            if "/" in date:
                date = date.split("/")
                month, day, year = int(date[0]), int(date[1]), int(date[2])
                if not 1 <= month <= 12:
                    continue
                if not 1 <= day <= 31:
                    continue
                return(year, month, day)
            # for Month DD, YYYY formated input
            if " " in date:
                date = date.split(" ")
                # to reject input if not specificly formated with "," after day
                if not "," in date[1]:
                    continue
                month, day, year = date[0], int(date[1].replace(",", "")), int(date[2])
                month = int(MONTHS.index(month)) + 1
                if not 1 <= month <= 12:
                    continue
                if not 1 <= day <= 31:
                    continue
                return(year, month, day)

        except KeyError:
            continue
        except  ValueError:
            continue

if __name__ == "__main__":
    main()