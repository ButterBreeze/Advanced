import tkinter as tk

# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
# import Tkinter as tk

window = tk.Tk()

dlblThingsCopied = tk.Label(window, text="The text that has been copied so far")
dlblThingsCopied.pack()



window.geometry("500x800")
window.mainloop()