def main():
    text = input()
    print(convert(text))

def convert(conv):
    emo = conv.replace(":)", "🙂")
    emo = emo.replace(":(", "🙁")
    return emo

main()