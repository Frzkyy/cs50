def main():
    clock = input(" ")
    schedule = convert(clock)

    if 7 <= schedule <= 8:
        print("breakfast time")
    elif 12 <= schedule <= 13:
        print("lunch time")
    elif 18 <= schedule <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour) + (float(minute)/60) 
    return hour


if __name__ == "__main__":
    main()