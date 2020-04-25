import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg="#d7dBe0", bd=2) #widget toolbar
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию',
                                    command=self.open_dialog, bg="#d7dBe0", bd=0,
                                    compound=tk.TOP) #widget button
        btn_open_dialog.pack(side=tk.LEFT)

        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg="#d7dBe0", bd=0,
                                    command=self.open_update_dialog,
                                    compound=tk.TOP)
        btn_edit_dialog.pack(side=tk.LEFT)

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

    def records(self, description, costs, amount):
        self.db.insert_data(description, costs, amount)
        self.view_records()

    def update_record(self, description, cost, amount):
        self.db.c.execute('''UPDATE finance
                             SET description=?, cost=?, amount=?
                             WHERE ID=?''', (description, cost, amount,
                                             self.tree.set(self.tree.selection()[0], "#1")))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''
                            SELECT * FROM finance
                          ''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


    @staticmethod
    def open_dialog():
        Child()

    @staticmethod
    def open_update_dialog():
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

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
        self.button_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.button_cancel.place(x=300, y=170)

        # widget - кнопка
        self.btn_ok = ttk.Button(self, text="Добавить")
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(description=self.entry_description.get(),
                                                                  costs=self.entry_money.get(),
                                                                  amount=self.combobox.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))
        self.btn_ok.destroy()
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
                '''
                    CREATE TABLE IF NOT EXISTS finance(
                      id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      description TEXT,
                      cost TEXT,
                      amount REAL) 
                '''
        )
        self.conn.commit()

    def insert_data(self, description, cost, amount):
        self.c.execute('''
                        INSERT INTO finance(description, cost, amount)
                        VALUES (?, ?, ?)
                        ''', (description, cost, amount))
        self.conn.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Household finance')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
