import tkinter as tk

window = tk.Tk()
window.title("Hola Mundo")
window.geometry("300x300")

hello = tk.Label(text="hola mundo")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()