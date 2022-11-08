from tkinter import *

main = Tk()

button = [[j for j in range(3)] for i in range (3)]
print('Button is {}'.format(button))



for i in range(3):
    for x in range(3):
        button[i][x] = Button(main,text ="x",font=('Arial',30))
        button[i][x].grid(row=i,column=x)
        print("Row is {} and Column is {}".format(i,x))
        
print("Button is {}".format(button))

main.mainloop()