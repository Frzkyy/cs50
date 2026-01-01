import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if hour := re.search(
            r"^(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)$",
            s,
        ):

            m1 = hour.group(2) or ":00"
            m2 = hour.group(5) or ":00"

            h1 = int(hour.group(1))
            h2 = int(hour.group(4))

            p1 = hour.group(3)
            p2 = hour.group(6)

            if p1 == "AM":
                if h1 == 12:
                    h1 = 0
            else:
                if h1 != 12:
                    h1 += 12

            if p2 == "AM":
                if h2 == 12:
                    h2 = 0
            else:
                if h2 != 12:
                    h2 += 12

            return f"{h1:02}{m1} to {h2:02}{m2}"

        else:
            raise ValueError

    except ValueError:
        raise


if __name__ == "__main__":
    main()
