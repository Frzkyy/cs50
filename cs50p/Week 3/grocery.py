items = {}

while True:
    try:
        thing = input("").strip().upper()
        if thing == "":
            break

        if thing in items:
            items[thing] += 1
        else:
            items[thing] = 1

    except EOFError:
        break

for item in sorted(items):
    print(items[item], item)
