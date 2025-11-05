def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    num = False
    if s.isnumeric(): return False
    elif 6 >= len(s) >= 2 and s.isalnum():
        for alpha in s:
            if alpha.isnumeric() and num == False:
                num = True
                if alpha == "0": return False
            if num == True and alpha.isalpha():
                return False
        return True
    else:
        return False
main()