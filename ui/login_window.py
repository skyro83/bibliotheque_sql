from tkinter import *
from tkinter import messagebox
from user.user_manager import check_login

def open_login_window(mode):
    login = Tk()
    login.geometry("300x200")
    login.title("Se connecter")

    l = Label(login, text="Identifiant")
    inputid = Text(login, height=1, width=25)

    l.pack()
    inputid.pack()

    l2 = Label(login, text="Mot de passe")
    inputmdp = Text(login, height=1, width=25)
    l2.pack()
    inputmdp.pack()

    def check_credentials():
        idi = inputid.get("1.0", "end")
        password = inputmdp.get("1.0", "end")
        if check_login(idi.strip(), password.strip()):
            messagebox.showinfo("Success", "Connexion réussie")
            mode.set("Mode: Admin")
            login.destroy()
        else:
            messagebox.showerror("Error", "Identifiant ou mot de passe incorrect")
            mode.set("Mode: User")

    login_b = Button(login, text="Se connecter", command=check_credentials)
    login_b.pack()

    login.mainloop()