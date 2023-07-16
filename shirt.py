from PIL import Image,ImageOps
import sys

def main():
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    if len(sys.argv) > 3:
        sys.exit("Too many Argument")
    elif len(sys.argv) < 3:
        sys.exit("Too few Argument")
    else:
        _,b = input_image.split('.')
        _,y = output_image.split('.')
        if (b == 'png' or b == 'jpg' or b == 'jpeg') and (y == 'png' or y == 'jpg' or y == 'jpeg'):
            if b == y:
                image_fitting(input_image,output_image)
            else:
                sys.exit("Give Same Extension")
        else:
            sys.exit("Enter a Valid Extension")

def image_fitting(before_image,after_image):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(before_image) as input:
            photo = ImageOps.fit(input,shirt.size)
            photo.paste(shirt,mask=shirt)
            photo.save(after_image)
    except FileNotFoundError:
        sys.exit(f"Could Not Find {before_image}")

if __name__ == "__main__":
    main()   