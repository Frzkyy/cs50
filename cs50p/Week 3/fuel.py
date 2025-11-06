while True:
    try:
        temp = input("Fraction: ")
        x,y = temp.split("/")
        x = int(x)
        y = int(y)
        if x < 0 or y < 0 or x > y:
            continue

        fuel = round(float(x/y) * 100)

        if fuel >= 99:
            print("F")
        elif fuel <= 1:
            print("E")
        else:
            print(f"{fuel}%")

        break
    except(ValueError,ZeroDivisionError):
        pass
    
