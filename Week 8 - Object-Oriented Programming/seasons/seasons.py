import sys, inflect
from datetime import date

p = inflect.engine()

class Minutes:
    def __init__(self, bday):
        self.bday = bday
        self.minutes = self.get_minutes()

    def __str__(self):
        return f"{p.number_to_words(self.minutes).replace(' and', '')} minutes".capitalize()

    @property
    def bday(self):
        return self._bday
    @bday.setter
    def bday(self, bday):
        try:
           year, month, day = map(int, bday.split("-"))
           self._bday = date(year, month, day)
        except ValueError:
            sys.exit("Invalid date")


    def get_minutes(self):
        today = date.today()
        timedelta = today - self.bday
        return round(timedelta.total_seconds() / 60)






def main():
    seconds = Minutes(input("Date of Birth: "))
    print(seconds)



if __name__ == "__main__":
    main()
