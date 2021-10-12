from Tkinter import *

def findArea():
    L = []
    L.append(int(num1.get()))
    L.append(int(num2.get()))
    answer.set(0.5 * L[0] * L[1])

window = Tk()
window.title("Area of Triangle")

num1 = StringVar()
num2 = StringVar()
answer = StringVar()

Label(window, text = "Base of Triangle: ").grid(row = 0, column = 0, pady = 5, sticky = E)
enternum1 = Entry(window, width = 8, textvariable = num1)
enternum1.grid(row = 0, column = 1, sticky = W)

Label(window, text = "Height of Triangle: ").grid(row = 1, column = 0, pady = 5, sticky = E)
enternum2 = Entry(window, width = 8, textvariable = num2)
enternum2.grid(row = 1, column = 1, sticky = W)


Label(window, text = "The area of the triangle is: ").grid(row = 4, column = 0, sticky = W)
ans = Entry (window, state = "readonly", width = 8, textvariable = answer)
ans.grid(row = 4, column = 1, sticky = W)

btnFind = Button(window, text = "Find the area of the triangle", command = findArea)
btnFind.grid(row = 3, column = 0, columnspan = 2, padx = 75, pady = 15)

window.mainloop()
