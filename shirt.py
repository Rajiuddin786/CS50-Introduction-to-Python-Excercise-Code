from PIL import Image,ImageOps
import sys

if len(sys.argv) != 3:
    sys.exit("Only two command-line arguments")

input_image = sys.argv[1]
output_image = sys.argv[2]

try:
   x,y = input_image.split('.')
   a,b = output_image.split('.')
except ValueError:
    sys.exit("Ente a Valid Extension")

if y != "jpg" and y != "jpeg" and y != "png" and b != "jpg" and b != "jpeg" and b != "png":
    sys.exit("Enter a Valid Extension")
if y != b:
    sys.exit("Must have same extension")

try:
    shirt = Image.open(input_image)
    size = shirt.size

    with Image.open("shirt.png") as pic:
        photo = ImageOps.fit(pic,size=(size[0],size[1]))
        photo.paste(shirt,shirt)
        photo.save(output_image)
    sys.exit(0)
except FileNotFoundError:
    sys.exit(f"File does not exit")