price = 50
while(price > 0):
    print(f"Amount Due: {price}")
    money = int(input("Insert Coin: "))
    if money in [5,10,25]:
        price = price - money
print(f"Change Owed: {price * -1}")
