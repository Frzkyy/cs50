import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r"<iframe.+src=\"(http|https)://(www\.)?youtube\.com/embed/([^\"]+)", s):
        return f"https://youtu.be/{link.group(3)}"

if __name__ == "__main__":
    main()
