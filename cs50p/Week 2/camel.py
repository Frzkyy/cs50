camel = input(" ").strip()

for snake in camel:
    if snake.isupper():
        print(f"_{snake.lower()}", end="")
    else:
        print(snake, end="")