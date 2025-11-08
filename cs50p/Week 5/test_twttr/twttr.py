def main():
    print(shorten("alpPhaAAaAAA[][][]"))


def shorten(word):
    twt = ""
    for alph in word:

        match alph.lower():
            case "a"|"i"|"u"|"e"|"o":
                continue
            case _:
                twt = twt + "" + alph
    return twt


if __name__ == "__main__":
    main()
