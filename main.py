from tkinter import *
from tkinter import messagebox
from login import check_login  # Assurez-vous que login.py est dans le même répertoire

def ad_open():
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
        else:
            messagebox.showerror("Error", "Identifiant ou mot de passe incorrect")

    login_b = Button(login, text="Se connecter", command=check_credentials)
    login_b.pack()

main = Tk()
main.geometry("500x500")
main.title('Bibliotheque Browser')

admin_login = Button(main, text="Administration", command=ad_open)
admin_login.place(x=50, y=50)

main.mainloop()
