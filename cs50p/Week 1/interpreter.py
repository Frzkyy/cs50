calc = input(" ")
x,y,z = calc.split(" ")

match y:
    case '+':
        print(float(x) + float(z))
    case '-':
        print(float(x) - float(z))
    case '*':
        print(float(x) * float(z))
    case '/':
        print(float(x) / float(z))
