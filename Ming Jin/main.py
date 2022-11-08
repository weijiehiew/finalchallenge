from tkinter import *

def colourbtn(i, j):
  global colour   
  if colour == 0:
    button[i][j].config(bg='grey99')
    value[i][j] = 0
  elif colour == 1: 
    button[i][j].config(bg='grey88')
    value[i][j] = 20
  elif colour == 2:
    button[i][j].config(bg='grey77')
    value[i][j] = 30
  elif colour == 3: 
    button[i][j].config(bg='grey66')
    value[i][j] = 40
  elif colour == 4:
    button[i][j].config(bg='grey44')  
    value[i][j] = 50
  elif colour == 5: 
    button[i][j].config(bg='grey33')
    value[i][j] = 60
  elif colour == 6:
    button[i][j].config(bg='grey11')
    value[i][j] = 70
  else: 
    button[i][j].config(bg='grey1')
    value[i][j] = 90

def change_colour(m): 
  global colour
  colour=m 

  print("colour is {}".format(colour))


def allwhite():
    for j in range(32):
        for i in range (32):
            button[i][j].config(bg='white')
            value[i][j] = 0

def allblack():
    for j in range(32):
        for i in range(32):
            button[i][j].config(bg ='grey1')
            value[i][j] = 90


def sendImage():
    global value
    print("Image has been printed, the values are.....")
 

def pat1():
  for i in range (32):
    for j in range (32):
      button[i][j].config(bg ='white')
      value[i][j] = 0
      if i == j: 
        button[i][j].config(bg='grey1')
        value[i][j] = 90
      elif i + j == 1: 
        button[i][j].config(bg='grey99')
        value[i][j] = 0
      elif i + j == 31: 
        button[i][j].config(bg='grey1')
        value[i][j] = 90


def pat2():
    for j in range(32):
        for i in range(32):
            if i == j:
                button[i][j].config(bg = 'grey99')
                value[i][j] = 0
            elif i - j <= 1:
                button[i][j].config(bg = 'grey66')
                value[i][j] = 40
            elif i + j >= 2:
                button[i][j].config(bg = 'grey33')  
                value[i][j] = 60
            else:
                button[i][j].config(bg = 'grey11')
                value[i][j] = 90
main = Tk()


#this variable to store the colour choice 
colour = 0

#3x3 btn
frame1 = Frame(main) 
frame1.grid(row=0, column=0)

#shades btn
frame2 = Frame(main) 
frame2.grid(row=0, column=1)

#colour btns
frame3 = Frame(main)
frame3.grid(row=1, columnspan=2)  

#send btn
frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) 

# 32x32 grid
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for j in range(32)] for i in range (32)]

for i in range (32):
  for j in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), bg='grey99', width=2, height=1, command=lambda r=i, c=j:colourbtn(r, c))
    button[i][j].grid(row=i, column=j)
    

# #shades button
white = Button(frame2, text="White", font=("Calibri, 12"), bg='grey99', width=13, height=2, command=lambda m=0:change_colour(m))
white.grid(row=0, column=0)
grey1 = Button(frame2, text="Grey1", font=("Calibri, 12"), bg='grey88', width=13, height=2, command=lambda m=1:change_colour(m))
grey1.grid(row=1, column=0)
grey2 = Button(frame2, text="Grey2", font=("Calibri, 12"), bg='grey77', width=13, height=2, command=lambda m=2:change_colour(m))
grey2.grid(row=2, column=0)
grey3 = Button(frame2, text="Grey3", font=("Calibri, 12"), bg='grey66', width=13, height=2, command=lambda m=3:change_colour(m))
grey3.grid(row=3, column=0)
grey4 = Button(frame2, text="Grey4", font=("Calibri, 12"), bg='grey44', width=13, height=2, command=lambda m=4:change_colour(m))
grey4.grid(row=4, column=0)
grey5 = Button(frame2, text="Grey5", font=("Calibri, 12"), bg='grey33', fg='white', width=13, height=2, command=lambda m=5:change_colour(m))
grey5.grid(row=5, column=0)
grey6 = Button(frame2, text="Grey6", font=("Calibri, 12"), bg='grey11', fg='white', width=13, height=2, command=lambda m=6:change_colour(m))
grey6.grid(row=6, column=0)
black = Button(frame2, text="Black", font=("Calibri, 12"), bg='grey1', fg='white', width=13, height=2, command=lambda m=7:change_colour(m))
black.grid(row=7, column=0)

#all white button
allwht = Button(frame3, text='All White', font = ("Calibri, 12"), bg='white',width = 13, height = 2,command = allwhite)
allwht.grid(row=0, column=0)

#all black button
allblk = Button(frame3, text='All Black', font = ("Calibri, 12"), bg='Black',fg = 'white',width = 13, height = 2, command = allblack)
allblk.grid(row=0, column=1)

#cross pattern
pattern1 = Button(frame3, text="Pattern 1",font= ("Calibri, 12"), bg='gold', width=13, height=2, command=pat1)
pattern1.grid(row=0, column=2)

#sequence button
pattern2 = Button(frame3, text='Pattern 2', font = ("Calibri, 12"), bg='pink',fg = 'black',width = 13, height = 2,command = pat2)
pattern2.grid(row=0, column=3)


#send btn
send = Button(frame4, text="Send Image", font= ("Calibri, 12"), width=13, height=2, command=sendImage )
send.grid(row=0, column=0)

# print("Button is {}".format(value))

main.mainloop()