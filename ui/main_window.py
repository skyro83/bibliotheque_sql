from tkinter import *
from ui.login_window import open_login_window
from ui.database_window import open_database_window

def open_main_window():
    main = Tk()
    main.geometry("500x500")
    main.title('Bibliotheque Browser')

    mode = StringVar()
    mode.set("Mode: User")

    gestion_b = Button(main, text="Gestion", command=open_database_window, state=DISABLED)
    gestion_b.place(x=100, y=50)

    def open_login():
        open_login_window(mode)
        # Après la connexion, vérifiez si l'utilisateur est en mode Admin
        if mode.get() == "Mode: Admin":
            # Si oui, activez le bouton de gestion
            gestion_b.config(state=NORMAL)

    admin_login = Button(main, text="Administration", command=open_login)
    admin_login.place(x=50, y=50)

    # Créez le bouton de gestion et cachez-le par défaut
    gestion_b = Button(main, text="Gestion", command=open_database_window)
    gestion_b.place(x=100, y=50)
    gestion_b.pack_forget()

    main.mainloop()