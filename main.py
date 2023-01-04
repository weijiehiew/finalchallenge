from tkinter import *
from tkinter import ttk

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

  print("Colour chosen is {}".format(colour))


def allwhite():
    for j in range(32):
        for i in range (32):
            button[i][j].config(bg='grey99')
            value[i][j] = 0

def allblack():
    for j in range(32):
        for i in range(32):
            button[i][j].config(bg ='grey1')
            value[i][j] = 90


def sendImage():
    global value
    print("Image has been printed, the values are.....")
    print(value)
 

def pattern():
    for i in range (32):
        for j in range (32):
            if i == j: 
                button[i][j].config(bg='grey1')
                value[i][j] = 90
            elif i + j == 31: 
                button[i][j].config(bg='grey1')
                value[i][j] = 90
            else:
                button[i][j].config(bg ='grey99')
                value[i][j] = 0



def seq():
    for j in range(32):
        for i in range(32):
            if i == 1 or i == 9 or i == 17 or i == 25:
                button[i][j].config(bg = 'grey88')
                value[i][j] = 20
            elif i == 2 or i == 10 or i == 18 or i == 26:
                button[i][j].config(bg = 'grey77')
                value[i][j] = 30
            elif i == 3 or i == 11 or i == 19 or i == 27:
                button[i][j].config(bg = 'grey66')
                value[i][j] = 40
            elif i == 4 or i == 12 or i == 20 or i == 28:
                button[i][j].config(bg = 'grey44')
                value[i][j] = 50
            elif i == 5 or i == 13 or i == 21 or i == 29:
                button[i][j].config(bg = 'grey33')
                value[i][j] = 60
            elif i == 6 or i == 14 or i == 22 or i == 30:
                button[i][j].config(bg = 'grey11')
                value[i][j] = 70
            elif i == 7 or i == 15 or i == 23 or i == 31:
                button[i][j].config(bg = 'grey1')
                value[i][j] = 90
            else:
                button[i][j].config(bg = 'grey99')
                value[i][j] = 0
            
def get_x_and_y(event):
   global lasx, lasy
   lasx, lasy = event.x, event.y

def paint(event):
    global lasx, lasy
    
    if colour == 0: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey99',width=4)  
    elif colour == 1:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey88',width=4)
        
    elif colour == 2:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey77',width=4)
    elif colour == 3: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey66',width=4)
    elif colour == 4:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey44',width=4)
    elif colour == 5: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey33',width=4)
    elif colour == 6:
        c.create_line((lasx,lasy, event.x, event.y),fill='grey11',width=4)
    else: 
        c.create_line((lasx,lasy, event.x, event.y),fill='grey11',width=4)

    lasx, lasy = event.x, event.y
    

def clearbtn():
    c.delete('all')

main = Tk()
main.title("Group D")

#A variable to store the colour choices 
colour = 0

notebook = ttk.Notebook(main) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2
tab3 = Frame(notebook) #new frame for tab 2

notebook.add(tab1,text="Grid")
notebook.add(tab2,text="Draw")
notebook.add(tab3,text="Tab 3")
notebook.grid(row=0, column = 0)

#32x32 buttons
frame1 = Frame(tab1) 
frame1.grid(row=0, column=0)

#shades buttons
frame2 = Frame(main) 
frame2.grid(row=0, column=1)

#colour buttons
frame3 = Frame(main)
frame3.grid(row=1, columnspan=2)  

#send button
frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) 

frame5 = Frame(tab2)
frame5.grid(row=0, column=0)

c = Canvas(tab2, width=443, height=380, bg='white')
c.grid(row=0, column=0)
# c.pack(anchor='nw', fill='both', expand=1)

c.bind('<Button-1>', get_x_and_y)
c.bind('<B1-Motion>',paint)

# 32x32 grid
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for j in range(32)] for i in range (32)]

for i in range (32):
  for j in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), bg='grey99', width=1, height=1, command=lambda r=i, c=j:colourbtn(r, c))
    button[i][j].grid(row=i, column=j)
    
clear = Button(frame2, text="Clear", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=0)

# shades button
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
xpattern = Button(frame3, text="X Pattern",font= ("Calibri, 12"), bg='gold', width=13, height=2, command=pattern)
xpattern.grid(row=0, column=2)

#sequence button
sequence = Button(frame3, text="Sequence", font = ("Calibri, 12"), bg='pink',fg = 'black',width = 13, height = 2,command = seq)
sequence.grid(row=0, column=3)


#send btn
send = Button(frame4, text="Send Image", font= ("Calibri, 12"), width=13, height=2, command=sendImage )
send.grid(row=0, column=0)


main.mainloop()