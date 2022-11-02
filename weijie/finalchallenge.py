from tkinter import *

def whitebutton(i,j):
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
    colour = m
    print('Colour is {}'.format(colour))

def allwhite():
    for j in range(3):
        for i in range (3):
            button[i][j].config(bg='white')

def allblack():
    for j in range(3):
        for i in range(3):
            button[i][j].config(bg = 'black')



main = Tk()

#Grid frame
frame1 = Frame(main)
frame1.grid(row=0, column=0)

#Colour palette frame
frame2 = Frame(main)
frame2.grid(row=0, column=1)

#Pattern frame
frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) 

#Send image button frame
frame4 = Frame(main)
frame4.grid(row=2, columnspan=2)

#3x3 grid
button = [[j for j in range(3)] for i in range (3)]

for i in range(3):
    for j in range(3):
        button[i][j] = Button(frame1,font=('Arial',30),width = 7, height = 3,command = lambda r=i, c=j:whitebutton(r,c))
        button[i][j].grid(row=i,column=j)
        print(button)
       


white = Button(frame2,text="White",font=('Calibri,12'),bg='grey99',width = 12, height = 2, command = lambda m=0:change_colour(m))
white.grid(row=0, column=0)
grey1 = Button(frame2,text="Grey 1",font=('Calibri,12'),bg='grey88',width = 12, height = 2, command = lambda m=1:change_colour(m))
grey1.grid(row=1, column=0)
grey2 = Button(frame2,text="Grey 2",font=('Calibri,12'),bg='grey77',width = 12, height = 2, command = lambda m=2:change_colour(m))
grey2.grid(row=2, column=0)
grey3 = Button(frame2,text="Grey 3",font=('Calibri,12'),bg='grey66',width = 12, height = 2, command = lambda m=3:change_colour(m))
grey3.grid(row=3, column=0)
grey4 = Button(frame2,text="Grey 4",font=('Calibri,12'),bg='grey44',width = 12, height = 2, command = lambda m=4:change_colour(m))
grey4.grid(row=4, column=0)
grey5 = Button(frame2,text="Grey 5",font=('Calibri,12'),bg='grey33',width = 12, height = 2, command = lambda m=5:change_colour(m))
grey5.grid(row=5, column=0)
grey6 = Button(frame2,text="Grey 6",font=('Calibri,12'),bg='grey11',fg = 'white',width = 12, height = 2, command = lambda m=6:change_colour(m))
grey6.grid(row=6, column=0)
black = Button(frame2,text="Black",font=('Calibri,12'),bg='grey1',fg = 'white',width = 12, height = 2, command = lambda m=7:change_colour(m))
black.grid(row=7, column=0)

#all white button
allwht = Button(frame3, text='All White', font = 'Arial,12',bg='white',width = 13, height = 2,command = allwhite)
allwht.grid(row=0, column=0)

#all black button
allblk = Button(frame3, text='All Black', font = 'Arial,12',bg='Black',fg = 'white',width = 13, height = 2, command = allblack)
allblk.grid(row=0, column=1)

#cross pattern X
crosspattern = Button(frame3, text='X Pattern', font = 'Arial,12',bg='yellow',width = 13, height = 2)
crosspattern.grid(row=0, column=2)

#sequence button
sequence = Button(frame3, text='Sequence', font = 'Arial,12',bg='pink',fg = 'black',width = 13, height = 2)
sequence.grid(row=0, column=3)


#Seend image button
send = Button(frame4,text='Send Image', font = 'Arial,12',width = 12, height = 2)
send.grid(row = 0, column = 0)




main.mainloop()