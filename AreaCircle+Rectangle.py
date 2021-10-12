from Tkinter import *

def findAreaCircle():
    L = []
    L.append(int(radius.get()))
    answerCircle.set(3.14 * (L[0] **2))

def findAreaRectangle():
    L = []
    L.append(int(width.get()))
    L.append(int(length.get()))
    answerRectangle.set(L[0] * L[1])

window = Tk()
window.title("Area Circle and Rectangle")

radius = StringVar()
answerCircle = StringVar()

Label(window, text = "Radius of Circle: ").grid(row = 0, column = 0, pady = 5, sticky = E)
enterradius = Entry(window, width = 8, textvariable = radius)
enterradius.grid(row = 0, column = 1, sticky = W)

btnFind = Button(window, text = "Find the area of the circle", command = findAreaCircle)
btnFind.grid(row = 3, column = 0, columnspan = 2, padx = 75, pady = 15)

Label(window, text = "The area of circle is: ").grid(row = 4, column = 0, sticky = W)
ans = Entry (window, state = "readonly", width = 8, textvariable = answerCircle)
ans.grid(row = 4, column = 1, sticky = W)

width = StringVar()
length = StringVar()
answerRectangle = StringVar()

Label(window, text = "Width of rectangle: ").grid(row = 30, column = 0, pady = 5, sticky = E)
enterwidth = Entry(window, width = 8, textvariable = width)
enterwidth.grid(row = 30, column = 1, sticky = W)

Label(window, text = "Length of rectangle: ").grid(row = 31, column = 0, pady = 5, sticky = E)
enterlength = Entry(window, width = 8, textvariable = length)
enterlength.grid(row = 31, column = 1, sticky = W)

btnFind = Button(window, text = "Find the area of the rectangle", command = findAreaRectangle)
btnFind.grid(row = 40, column = 0, columnspan = 2, padx = 75, pady = 15)

Label(window, text = "The area of rectangle is: ").grid(row = 50, column = 0, sticky = W)
ans = Entry (window, state = "readonly", width = 8, textvariable = answerRectangle)
ans.grid(row = 50, column = 1, sticky = W)

window.mainloop()

