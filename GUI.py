from tkinter import *


class Gui:

    def __init__(self):
        self.root = Tk()

    def window(self):
        root = self.root
        spsok = Toplevel(root)
        spsok.title('Список акаунтів')
        spsok.geometry("500x200")
        spsok.grab_set()
        spsok.focus_set()
        but = Button(spsok, text='Зберегти в файл', font='Arial 12')
        but.grid(column=1, row=3)


    def login(self):
        root = self.root
        window = self.window
        root.title('Likes!')
        root.geometry("600x300")
        m = Menu(root)
        root.config(menu=m)
        m.add_cascade(label="Добавить", command=window)

        m.title = Label(root, text='InstagramBot', width=20, height=1, fg='orange', font='arial 18')
        m.title.pack()

        login = Entry(root, borderwidth=2, width=30)
        login.pack()

        password = Entry(root, borderwidth=2, width=30, show='*')
        password.pack()

        button1 = Button(root, text='LOG IN', width=16, height=1, bg='light gray', fg='black', font='arial 14')
        button1.pack()

        root.mainloop()


Gui().login()
