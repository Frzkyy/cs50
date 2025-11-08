import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        tries = 0
        x, y = generate_integer(level)
        ans = x + y

        while tries < 3:
            try:
                calc = int(input(f"{x} + {y} = "))
                if calc == ans:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                tries += 1
                print("EEE")

        if tries == 3:
            print(f"{x} + {y} = {ans}")

    print(score)


def get_level():
    while True:
        try:
            lvl = int(input())
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
