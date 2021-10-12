from Tkinter import *

def concorde(event):
    ind = Sch.index(lb.get(lb.curselection()))
    lb["bg"] = BC[ind]
    lb["fg"] = FC[ind]
    m["bg"] = BC[ind]
    m["fg"] = FC[ind]
    Mascot.set(M[ind])

w = Tk()
w.title("Concorde District")

School = StringVar()
Mascot = StringVar()

Sch=['School1','School2','School3','School4','School5','School6']
M=['Wildcats','Chargers','Warhawks','Cougars','Seahawks','Bulldogs']
BC=['light blue','purple','red','gold','green','black']
FC = ["white", "white", "black", "red", "blue", "white"]

School.set(tuple(Sch))

Label(w, text = "School: ").grid(row = 0, column = 0, pady = 1, sticky = W)
lb = Listbox(w, width = 20, height = 6, listvariable = School)
lb.grid(row = 1, column = 0, padx = 1, pady = 1)

Label(w, text = "Mascot: ").grid(row = 0, column = 1, pady = 1, sticky = W)
Mascot.set("Mascot")
m = Entry(w, width = 20, textvariable = Mascot)
m.grid(row = 1, column = 1, sticky = W)

lb.bind("<<ListboxSelect>>",concorde)
w.mainloop()
    
