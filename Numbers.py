from Tkinter import *

def findLargest():
    L = []
    L.append(int(num1.get()))
    L.append(int(num2.get()))
    L.append(int(num3.get()))

    answer.set(max(L))

window = Tk()
window.title("Largest Number")

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
answer = StringVar()

Label(window, text = "First number: ").grid(row = 0, column = 0, pady = 5, sticky = E)
enternum1 = Entry(window, width = 8, textvariable = num1)
enternum1.grid(row = 0, column = 1, sticky = W)

Label(window, text = "Second number: ").grid(row = 1, column = 0, pady = 5, sticky = E)
enternum2 = Entry(window, width = 8, textvariable = num2)
enternum2.grid(row = 1, column = 1, sticky = W)

Label(window, text = "Third number: ").grid(row = 2, column = 0, pady = 5, sticky = E)
enternum3 = Entry(window, width = 8, textvariable = num3)
enternum3.grid(row = 2, column = 1, sticky = W)

Label(window, text = "The largest number is: ").grid(row = 4, column = 0, sticky = W)
ans = Entry (window, state = "readonly", width = 8, textvariable = answer)
ans.grid(row = 4, column = 1, sticky = W)

btnFind = Button(window, text = "Find the Largest", command = findLargest)
btnFind.grid(row = 3, column = 0, columnspan = 2, padx = 75, pady = 15)

window.mainloop()
