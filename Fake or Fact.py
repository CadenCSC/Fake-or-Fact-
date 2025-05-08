import tkinter as tk

root = tk.Tk()
root.title("Fake or Fact")
root.geometry('1350x800')

lbl = tk.Label(root, text = "Fake or Fact")
lbl.grid()

def fakeclicked():
    lbl.configure(text= "FAKE")

def factclicked():
    lbl.configure(text= "FACT")
    
btnfake = tk.Button(root, text = "FAKE" , bg = "red", fg = "White", padx = 200, pady = 40, command=fakeclicked)
btnfake.place(x = 40, y = 650)

btnfact = tk.Button(root, text = "FACT", bg = "green", fg = "White", padx=  200, pady = 40, command=factclicked)
btnfact.place(x = 875, y =650)

root.mainloop()