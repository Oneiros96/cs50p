import random

def main():
    level = get_level()
    if level == 1:
        play(level)
    else:
        rnd_number = random.randrange(1, level)
        play(rnd_number)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 0:
                continue
            return(level)
        except ValueError:
            pass

def play(number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == 0:
                continue
            match guess:
                case x if x < number:
                    print("Too small!")
                case x if x > number:
                    print("Too large!")
                case x if x == number:
                    print("Just right!")
                    return
        except ValueError:
            pass

if __name__ == "__main__":
    main()

