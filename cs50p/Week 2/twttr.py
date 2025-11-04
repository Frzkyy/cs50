tweet = input("Input: ")
twt = ""
for alph in tweet:

    match alph.lower():
        case "a"|"i"|"u"|"e"|"o":
            continue
        case _:
            twt = twt + "" + alph
print(twt)