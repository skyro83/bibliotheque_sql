from tkinter import *
from ui.login_window import open_login_window

def open_main_window():
    main = Tk()
    main.geometry("500x500")
    main.title('Bibliotheque Browser')

    mode = StringVar()
    mode.set("Mode: User")

    admin_login = Button(main, text="Administration", command=lambda: open_login_window(mode))
    admin_login.place(x=50, y=50)

    main.mainloop()