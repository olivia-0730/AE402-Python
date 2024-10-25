import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

window.title("My first GUI APP")

window.geometry('300x300')

label = tk.Label(window, text="Class", bg="#ffe5ec",fg="#a2d2ff")
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

def clickme():
    tkinter.messagebox.showinfo(title="hint", message="ouch")

button = tk.Button(window, text="Yes", command=clickme)
button.pack()

window.mainloop()