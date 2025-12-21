import sys
from PIL import Image, ImageOps

# Argument count check
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# File extension validation
if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid input")
if not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")

# Extension comparison (NO os.path)
ext1 = sys.argv[1].split(".")[-1].lower()
ext2 = sys.argv[2].split(".")[-1].lower()

if ext1 != ext2:
    sys.exit("Input and output have different extensions")

# Image processing
try:
    input_img = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    input_img = ImageOps.fit(
        input_img,
        shirt.size,
        method=Image.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )

    shirt_x = (input_img.width - shirt.width) // 2
    shirt_y = (input_img.height - shirt.height) // 2

    input_img.paste(shirt, (shirt_x, shirt_y), shirt)
    input_img.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
