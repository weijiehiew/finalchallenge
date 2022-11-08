# 32 x 32 GUI

## First look at the 32 by 32 GUI
![Alt text](../../../../../../../../C:/Users/65844/OneDrive/Documents/GitHub/finalchallenge/32%20x%2032%20GUI/images/32x32.jpg)

## Purpose of the 32 x 32 GUI
The purpose of this 32 x 32 GUI is to allow users to be able to colour the 32 x 32 grid with different shades of grey. They will then be able to send the image out which will correspond with the 32 x 32 polarizing dishes.

<br>

## Getting started

```
from tkinter import *

main = Tk()

main.mainloop()
```

## 32 by 32 Grid

![Alt text](../../../../../../../../C:/Users/limmi/OneDrive/Documents/GitHub/finalchallenge/32%20x%2032%20GUI/images/32x32.jpg)

```
button = [[j for j in range(32)] for i in range(32)]

value = [[0 for j in range(32)] for i in range (32)]

for i in range (32):
  for j in range (32):
    button[i][j] = Button(frame1, font=("Calibri, 5"), bg='grey99', width=2, height=1, command=lambda r=i, c=j:colourbtn(r, c))
    button[i][j].grid(row=i, column=j)

```

