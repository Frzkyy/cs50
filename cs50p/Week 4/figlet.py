from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in figlet.getFonts():
        txt = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(txt))
    else:
        print("Invalid Usage")
        sys.exit(1)
elif len(sys.argv) == 1:
    txt = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(txt))
else:
    print("Invalid Usage")
    sys.exit(1)
