import random


def main():
    questions = 10
    score = 0
    chances = 3
    lvl = get_level()
    while questions != 0:
        if chances == 3:
            x, y = generate_integer(lvl)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                questions = questions - 1
                score = score + 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3
            questions = questions - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            number = int(input("level: "))
            if 1 <= number <= 3:
                return number
        except:
            pass


def generate_integer(lvl):
    if lvl == 1:
        p = random.randint(0, 9)
        q = random.randint(0, 9)
    elif lvl == 2:
        p = random.randint(10, 99)
        q = random.randint(10, 99)
    elif lvl == 3:
        p = random.randint(100, 999)
        q = random.randint(100, 999)
    else:
        p, q = None, None
    return p, q


if __name__ == "__main__":
    main()
