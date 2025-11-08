def main():
    user_input = input("Fraction: ")
    fuel_percentage_int = convert(user_input)
    gauge_reading = gauge(fuel_percentage_int)
    print(gauge_reading)


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x < 0 or y < 0 or x > y:
            raise ValueError

        return round((x / y) * 100)

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(fuel):
    if fuel >= 99:
        return "F"
    elif fuel <= 1:
        return "E"
    else:
        return f"{fuel}%"


if __name__ == "__main__":
    main()
