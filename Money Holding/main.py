import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg="#d7dBe0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию',
                                    command=self.open_dialog, bg="#d7dBe0", bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

    @staticmethod
    def open_dialog():
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Добавить доходы/расходы")
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Household finance')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
