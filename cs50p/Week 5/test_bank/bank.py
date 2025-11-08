def main():
    print(value("aalo"))


def value(greeting):
    text = greeting.lower().strip()

    if text.count('hello', 0,5) == 1:
        return "$0"
    elif text.count('h',0,1) >= 1:
        return "$20"
    else:
        return "$100"



if __name__ == "__main__":
    main()
