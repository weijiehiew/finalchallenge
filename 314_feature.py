from tkinter import *
from PIL import Image, ImageOps

# import time
# import paho.mqtt.client as mqtt

# def on_publish(client, userdata, mid):
#     print("message published")

# def pubpic(output):
#     k = output
#     msg = str(k)
#     pubMsg = client.publish(
#         topic='studentpi/team4', #Please change according to your respective Group  
#         payload=msg.encode('utf-8'),
#         qos=0,
#     )

#     pubMsg.wait_for_publish()
#     print(pubMsg.is_published())

def img_change(m):
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
        #smallImage.show()

        ## Blow it back up to original photo size (32 x 32 pixels upscale)
        resultImage = smallImage.resize(myImage.size, Image.NEAREST)
        resultImage.show()


def startshow():
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
        #smallImage.show()

        ## Blow it back up to original photo size (32 x 32 pixels upscale)
        resultImage = smallImage.resize(myImage.size, Image.NEAREST)
        resultImage.show()
        


main = Tk()
main.title("Group D's Love Story Show")
main.config(bg="skyblue")



#image
frame1 = Frame(main, width=650, height=400, bg='grey') 
frame1.grid(row=0, column=0, padx=10, pady=5)

#startshowbtn
frame2 = Frame(main, width=650, height=100, bg="grey") 
frame2.grid(row=0, column=1, padx=10, pady=5)

#allimagebuttons
frame3 = Frame(main, width=100, height=400, bg="grey")
frame3.grid(row=1, columnspan=2, padx=10, pady=5) 

Label(frame1, width=25, height=25, bg="grey").grid(row=0, column=0)

#open images
pic1 = PhotoImage(file="Resources/1.png")
pic2 = PhotoImage(file="Resources/2.png")
pic3 = PhotoImage(file="Resources/3.png")
pic4 = PhotoImage(file="Resources/4.png")
pic5 = PhotoImage(file="Resources/5.png")
pic6 = PhotoImage(file="Resources/6.png")
pic7 = PhotoImage(file="Resources/7.png")
pic8 = PhotoImage(file="Resources/8.png")
pic9 = PhotoImage(file="Resources/9.png")
pic10 = PhotoImage(file="Resources/10.png")
pic11 = PhotoImage(file="Resources/11.png")
pic12 = PhotoImage(file="Resources/12.png")
pic13 = PhotoImage(file="Resources/13.png")
pic14 = PhotoImage(file="Resources/14.png")
pic15 = PhotoImage(file="Resources/15.png")
pic16 = PhotoImage(file="Resources/16.png")

#resize the images
image1 = pic1.subsample(6, 6)
image2 = pic2.subsample(6, 6)
image3 = pic3.subsample(6, 6)
image4 = pic4.subsample(6, 6)
image5 = pic5.subsample(6, 6)
image6 = pic6.subsample(6, 6)
image7 = pic7.subsample(6, 6)
image8 = pic8.subsample(6, 6)
image9 = pic9.subsample(6, 6)
image10 = pic10.subsample(6, 6)
image11 = pic11.subsample(6, 6)
image12 = pic12.subsample(6, 6)
image13 = pic13.subsample(6, 6)
image14 = pic14.subsample(6, 6)
image15 = pic15.subsample(6, 6)
image16 = pic16.subsample(6, 6)


Label(frame2, text="Image 1",font=("Calibri, 20")).grid(row=0, column=0)
image1button = Button(frame2, image=image1, command=lambda m=1:img_change(m))
image1button.grid(row=0, column=0, padx=10, pady=10)

image2button = Button(frame2, image=image2, command=lambda m=2:img_change(m))
image2button.grid(row=0, column=1)

image3button = Button(frame2, image=image3, command=lambda m=3:img_change(m))
image3button.grid(row=0, column=2)

image4button = Button(frame2, image=image4, command=lambda m=4:img_change(m))
image4button.grid(row=0, column=3)

image5button = Button(frame2, image=image5, command=lambda m=5:img_change(m))
image5button.grid(row=1, column=0)

image6button = Button(frame2, image=image6, command=lambda m=6:img_change(m))
image6button.grid(row=1, column=1)

image7button = Button(frame2, image=image7, command=lambda m=7:img_change(m))
image7button.grid(row=1, column=2)

image8button = Button(frame2, image=image8, command=lambda m=8:img_change(m))
image8button.grid(row=1, column=3)

image9button = Button(frame2, image=image9, command=lambda m=9:img_change(m))
image9button.grid(row=2, column=0)

image10button = Button(frame2, image=image10, command=lambda m=10:img_change(m))
image10button.grid(row=2, column=1)

image11button = Button(frame2, image=image11, command=lambda m=11:img_change(m))
image11button.grid(row=2, column=2)

image12button = Button(frame2, image=image12, command=lambda m=12:img_change(m))
image12button.grid(row=2, column=3)

image13button = Button(frame2, image=image13, command=lambda m=13:img_change(m))
image13button.grid(row=3, column=0)

image14button = Button(frame2, image=image14, command=lambda m=14:img_change(m))
image14button.grid(row=3, column=1)

image15button = Button(frame2, image=image15, command=lambda m=15:img_change(m))
image15button.grid(row=3, column=2)

image16button = Button(frame2, image=image16, command=lambda m=16:img_change(m))
image16button.grid(row=3, column=3)

start = Button(frame3, text="Start Show!",font=("Calibri, 12"), bg='pink', width=13, height=2, command=startshow)
start.grid(rowspan =1 , columnspan = 4)

main.mainloop()