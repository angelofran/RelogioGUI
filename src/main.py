from tkinter import *
import time
import os

# Configurações iniciais
window = Tk()
window.title(f"{os.getlogin()} Watch")
window.geometry("400x250")
window.minsize(500, 250)
window.maxsize(500, 250)
window.configure(background="#333")
window.iconbitmap(fr'{os.getcwd()}\src\static\images\clock.ico')


# Interface
# Functions
def get_data():
    data = time.strftime("%I:%m:%S %p")
    mainText3.config(text=data)
    mainText3.after(1000, get_data)


mainText1 = Label(master=window, background="#333", foreground="#fff", text=f"Hello, {os.getlogin()}!",
                  font=('Montserrat', 16))
mainText1.pack(pady=20)

mainText2 = Label(
    master=window,
    background="#333",
    foreground="#fff",
    text=f'{time.strftime("%A")}, {time.strftime("%B")} of {time.strftime("%d")} of {time.strftime("%Y")}.',
    font=('Montserrat', 16)
)

mainText2.pack()

mainText3 = Label(
    master=window,
    background="#333",
    foreground="#fff",
    font=('Montserrat', 50)
)

mainText3.pack(pady=20)

get_data()

# Loop
window.mainloop()
