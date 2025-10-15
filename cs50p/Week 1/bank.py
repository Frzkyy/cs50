text = input(" ").lower().strip()

if text.count('hello', 0,5) == 1:
    print("$0")
elif text.count('h',0,1) >= 1:
    print("$20")
else:
    print("$100") 
