from tkinter import *

def whitebtn(i, j):
  global colour   
  if colour == 0:
    button[i][j].config(bg='grey99')
  elif colour == 1: 
    button[i][j].config(bg='grey88')
  elif colour == 2:
    button[i][j].config(bg='grey77')
  elif colour == 3: 
    button[i][j].config(bg='grey66')
  elif colour == 4:
    button[i][j].config(bg='grey44')  
  elif colour == 5: 
    button[i][j].config(bg='grey33')
  elif colour == 6:
    button[i][j].config(bg='grey11')
  else: 
    button[i][j].config(bg='grey1')

def change_colour(m): 
  global colour
  colour=m 

  print("colour is {}".format(colour))

def allwht():
  for i in range (3):
    for j in range (3):
      button[i][j].config(bg='grey99')

def allblk():
  for i in range (3):
    for j in range (3):
      button[i][j].config(bg='grey1')

def pattern():
  for i in range (3):
    for j in range (3):
      if i == j: 
        button[i][j].config(bg='grey1')
      elif i + j == 1: 
        button[i][j].config(bg='grey99')
      elif i + j == 2: 
        button[i][j].config(bg='grey1')
      elif i + j == 3:
        button[i][j].config(bg='grey99')
# colour_list=['grey99', 'grey88', 'grey77', 'grey66', 'grey44', 'grey33', 'grey11', 'grey1']
# colour_list=k   
def sequence():
  for i in range (3):
    for j in range (3): 
      if i + j == 0:
         button[i][j].config(bg='grey99')
      elif i == 0:
        if j == 1:
          button[i][j].config(bg='grey88')
      elif i == 0:
        if j == 2:
          button[i][j].config(bg='grey77')
      elif i == 1:
        if j == 0:
          button[i][j].config(bg='grey66')
      elif i == 1:
        if j == 1:
          button[i][j].config(bg='grey44')
      elif i == 1:
        if j == 2:
          button[i][j].config(bg='grey33')
      elif i == 2:
        if j == 0:
          button[i][j].config(bg='grey11')
      elif i == 2:
        if j == 1:
          button[i][j].config(bg='grey1')
      elif i + j == 4:
        button[i][j].config(bg='grey99')

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

# 3x3 grid
button = [[j for j in range(3)] for i in range(3)]
value = [(0 for j in range(3)) for i in range(3)]

for i in range (3):
  for j in range (3):
    button[i][j] = Button(frame1, font=("Calibri, 20"), bg='grey99', width=7, height=3, command=lambda r=i, c=j:whitebtn(r, c))
    button[i][j].grid(row=i, column=j)

    print(button)

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

# # #colour button
allwhite = Button(frame3, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

xpattern = Button(frame3, text="X Pattern",font=("Calibri, 12"), bg='gold', width=13, height=2, command=pattern)
xpattern.grid(row=0, column=2)

seq = Button(frame3, text="Sequence",font=("Calibri, 12"), bg='magenta', width=13, height=2, command=sequence)
seq.grid(row=0, column=3)

#send btn
send = Button(frame4, text="Send Image", font=("Calibri, 12"), width=13, height=2)
send.grid(row=0, column=0)

print("Button is {}".format(value))

main.mainloop()