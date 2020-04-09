import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg="#d7dBe0", bd=2) #widget toolbar
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию',
                                    command=self.open_dialog, bg="#d7dBe0", bd=0,
                                    compound=tk.TOP) #widget button
        btn_open_dialog.pack(side=tk.LEFT)

        #widget
        self.tree = ttk.Treeview(self, column=('ID', 'description', 'cost', 'amount'),
                                 height=15, show='headings')
        # доп.параметры для созданных колонок
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('cost', width=150, anchor=tk.CENTER)
        self.tree.column('amount', width=100, anchor=tk.CENTER)

        # Придадим название колонкам
        self.tree.heading("ID", text='ID')
        self.tree.heading('description', text="наименование")
        self.tree.heading('cost', text="Статья доходов\расходов")
        self.tree.heading('amount', text="Сумма")

        self.tree.pack()

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

        # widget label (надписи)
        label_description = tk.Label(self, text="Наименования")
        label_description.place(x=50, y=50)

        label_select = tk.Label(self, text="Статья доходов\расходов")
        label_select.place(x=50, y=80)

        label_sum = tk.Label(self, text="Сумма")
        label_sum.place(x=50, y=110)

        # widget для ввода данных
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        # widget с выпадающим списком
        self.combobox = ttk.Combobox(self, values=['Доход', "Расход"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        # widget для ввода суммы
        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        # widget - кнопка
        button_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        button_cancel.place(x=300, y=170)

        # widget - кнопка
        btn_ok = ttk.Button(self, text="Добавить")
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>')

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
