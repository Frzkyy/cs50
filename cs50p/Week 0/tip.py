def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    money = d.replace('$', '')
    return float(money)

def percent_to_float(p):
    pers = float(p.replace('%', ''))
    pers = pers / 100
    return pers
    
main()