price = 50
while(price > 0):
    print(f"Amount Due: {price}")
    money = int(input("Insert Coin: "))
    if(money == 5 or money == 10 or money == 25):
        price = price - money
print(f"Change Owned: {price * -1}")
