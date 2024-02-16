from tkinter import *
from database.db_manager import get_all_databases

def open_database_window():
    db_window = Tk()
    db_window.geometry("500x500")
    db_window.title('Database Management')

    databases = get_all_databases()
    for db in databases:
        label = Label(db_window, text=db)
        label.pack()

    db_window.mainloop()