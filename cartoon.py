from tkinter import *
from PIL import Image, ImageOps
from student_pub import *

def middleman(Images):
	#print(Image)
	myImage = Image.open(Images)
	## greyscale image file
	greyImage = ImageOps.grayscale(myImage)
	#greyImage.show()

	## Limiting to 8 shades of greyscale colour
	greyQuantize = greyImage.quantize(8)
	#greyQuantize.show()

	## resize to 32 x 32 pixels
	smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
	#smallImage.show()

	## Blow it back up to original photo size (32 x 32 pixels upscale)
	resultImage = smallImage.resize(myImage.size, Image.NEAREST)
	#resultImage.show()

	## Write Image to save .png file
	resultImage.save('cartoon.png')

	# Retrieving pixel value and formating it into list of list
	x = 32; k = 0; outputValue = [0 for i in range(x)]
	for i in range(x):
  	  outputValue[i] = [0 for j in range(x)]
	pixValue = list(smallImage.getdata())

	for i in range(x):
   	 for j in range(x):
	        outputValue[i][j] = pixValue[k]
	        k = k + 1;

	print(outputValue)
	pubpic(outputValue)








