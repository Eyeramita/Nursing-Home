from tkinter import *

root = Tk()

root.title('Booking Nursing-Home')
root.geometry('300x200')#size's window
root.configure(background="white")
Label(root, text="Choose desired service", font=("Arial", 18), bg="white").pack()

def page():
    meet = Tk()
    meet.title('Booking Nursing-Home')
    meet.geometry('800x600')
    meet.configure(background="white")
    Label(meet, text="Information", font=("Arial", 16), bg="white").grid(row=0, column=5)
    Label(meet,text="Name", font=(18), bg="white").grid(row=1, column=1)
    Label(meet,text="Age", font=(18), bg="white").grid(row=2, column=1)
    Label(meet,text="Desease", font=(18), bg="white").grid(row=3, column=1)
    Label(meet,text="Bedridden", font=(18), bg="white").grid(row=4, column=1)
    Label(meet,text="Neck piercing", font=(18), bg="white").grid(row=5, column=1)


Var1 = IntVar()
A1 = Checkbutton(root, text="Shelter the Center", variable=Var1, font=(18), bg="white", command=page)
A1.pack(anchor=W, padx=10, pady=10)
Var2 = IntVar()
A2 = Checkbutton(root, text="Send Staff to the patient's home", variable=Var2, font=(18), bg="white")
A2.pack(anchor=W, padx=10, pady=10)



root.mainloop()

 