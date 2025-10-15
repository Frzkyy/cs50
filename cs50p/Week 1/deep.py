text = input(" ").lower().strip()

match text:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")
