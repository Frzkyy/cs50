import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
            target = random.randint(1,level*10)
            break
        except ValueError:
            pass
    
    while True:
        try:
            guess = int(input("Guess: "))

            if guess < 1:
                raise ValueError
            elif guess == target:
                print("Just right!")
                break
            elif guess < target:
                print("Too small!")
            elif guess > target:
                print("Too large!")
        except ValueError:
            pass
    


main()