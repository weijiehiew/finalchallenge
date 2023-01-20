# Tested on Raspberry Pi 4 Model B
# Huats Club 2022 for the Pixel-Tint Project
from tkinter import *
from PIL import Image, ImageOps
# from studentpub import *
main = Tk()
## open image file
myImage = Image.open('Resources/1.png')
myImage.show()

## greyscale image file
greyImage = ImageOps.grayscale(myImage)
#greyImage.show()

## Limiting to 8 shades of greyscale colour
greyQuantize = greyImage.quantize(8)
#greyQuantize.show()

## resize to 32 x 32 pixels
smallImage = greyQuantize.resize((32,32), Image.BILINEAR)

#greyQuantize.show()

## Blow it back up to original photo size (32 x 32 pixels upscale)
resultImage = smallImage.resize(myImage.size, Image.NEAREST)
resultImage.show()

## Write Image to save .png file
#resultImage.save('cartoon.png')

# Retrieving pixel value and formating it into list of list
x = 32; k = 0; outputValue = [0 for i in range(x)]
for i in range(x):
    outputValue[i] = [0 for j in range(x)]
pixValue = list(smallImage.getdata())

for i in range(x):
    for j in range(x):
        outputValue[i][j] = pixValue[k]
        k = k + 1

print(outputValue)
# pubpic(outputValue)

main.mainloop()









