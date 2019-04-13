from tkinter import *
import IB
import Main


class Gui:

    def __init__(self):
        self.root = Tk()

    def login(self):
        root = self.root
        window = self.window
        root.title('subscribe!')
        root.geometry("600x300")
        # Меню з віджетами
        m = Menu(root)
        root.config(menu=m)
        m.add_cascade(label="Додати задачу", command=window)
        # Фон пнг
        C = Canvas(root, bg="blue")
        filename = PhotoImage(
            file="C:\\Users\\teria\\Downloads\\UNIC\\Programming\\Python_programm\\InstagramBot\\image.png")
        background_label = Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        # Вхід в Instagram
        login = Entry(root, borderwidth=2, bd=2, width=30, font="Arial 14")
        login.place(x=350, y=70, height=30, width=200)
        password = Entry(root, borderwidth=2, width=30, font="Arial 14", show='*')
        password.place(x=350, y=110, height=30, width=200)

        def enter():
            Main.username = login.get()
            Main.password = password.get()

        button1 = Button(root, text='LOG IN', width=16, height=1, bg='white', fg='red', font='arial 14', command=enter)
        button1.place(x=350, y=160, height=30, width=200)

        mainloop()

    def window(self):
        root = self.root
        spsok = Toplevel(root)
        spsok.title('Додати задачу')
        spsok.geometry("500x200")

        mark1 = BooleanVar()
        mark1.set(0)
        Checkbutton(spsok, text="Відписатися від всіх", variable=mark1, onvalue=1, offvalue=0).pack(anchor=W)

        mark2 = BooleanVar()
        mark2.set(0)
        Checkbutton(spsok, text="Підписатися на всіх зі списку", variable=mark2, onvalue=1, offvalue=0).pack(anchor=W)

        def mark():
            if mark1.get() == 1:
                ig = IB.InstagramBot(Main.username, Main.password, *Main.follower)
                ig.login()
                ig.unsubscribe()
            if mark2.get() == 1:
                ig = IB.InstagramBot(Main.username, Main.password, *Main.follower)
                ig.login()
                ig.subscribe()
            if mark1.get() == 1 and mark2.get() == 1:
                ig = IB.InstagramBot(Main.username, Main.password, *Main.follower)
                ig.login()
                ig.unsubscribe()
                ig.subscribe()

        but = Button(spsok, text='Виконати', font='Arial 12', command=mark)
        but.place(x=100, y=150)
        but.pack()


Gui().login()
