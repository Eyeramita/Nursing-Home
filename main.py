import tkinter as tk

window = tk.Tk()
window.title('Booking Nursery')
window.minsize(width = 400, height = 400)

title_label = tk.Label(master = window, text = "Desired Service")
title_label.pack()

window.mainloop()
