import random
import sys

def main():
    level = get_level()
    score = play(level)
    print(f"Score: {score}")
    sys.exit()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level and level < 4:
                return(level)
        except ValueError:
            pass

def play(level):
    problem_counter = 0
    score = 0
    while problem_counter < 10:
        problem_counter += 1
        problem, answer = get_problem(level)
        guess_counter = 0
        while guess_counter < 3:
            user_answer = input(problem)
            if user_answer == answer:
                score += 1
                break
            else:
                print("EEE")
                guess_counter += 1
                if guess_counter == 3:
                    print(f"{problem}{answer}")
                continue
    return(score)


def get_problem(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    problem = f"{x} + {y} = "
    answer = str(x + y)
    return(problem, answer)

if __name__ == "__main__":
    main()