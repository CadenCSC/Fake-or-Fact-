import tkinter as tk

root = tk.Tk()
root.title("Fake or Fact")
root.geometry('1350x800')

lbl = tk.Label(root, text = "Fake or Fact")
lbl.grid()

def clicked():
    lbl.configure(text= "FAKE")

btn = tk.Button(root, text = "FAKE" ,
                fg = "red", command=clicked)

btn.grid(column=2, row=10)

root.mainloop()