from inflect import engine
p = engine()
name = []
#kadie

 
while True:
    try:
        ip = input("Name: ")
        name.append(ip)
    except EOFError:
        if len(name) == 1:
            print(f"Adieu, adieu, to {name[0]}")
        else:
            print(f"Adieu, adieu, to {p.join(name)}")
        break
""" """ 
"""
"""
"""
aloooha
"""
"""
alooha """