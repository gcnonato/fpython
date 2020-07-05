import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

conn = sqlite3.connect('C:\sistema_salao\DataBase\my_database.db')
c = conn.cursor()
result = c.execute('SELECT MAX (id) from forneced')
for r in result:
  id = r[0]


class Fornecedor:
  def __init__(self, master, *args, **kw):
    self.master = master

    self.frame1 = Frame(master, width=1000, height=50,
                        bg='#222125', bd=1, relief='raise')
    self.frame1.pack(side=TOP)
    self.frame2 = Frame(master, width=1000, height=50,
                        bg='#222125', bd=1, relief='raise')
    self.frame2.pack(side=BOTTOM)

    self.label1 = Label(self.frame1, text='Cadastro de Fornecedor', font='arial 25 bold', bg='#222125', fg='white')
    self.label1.place(x=300, y=0)

    self.e_fornecedor = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_fornecedor.place(x=30, y=100)
    self.la_fornecedor = Label(master, text='Fornecedor:', font=('arial 9 bold'))
    self.la_fornecedor.place(x=30, y=69)

    self.e_email = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_email.place(x=30, y=150)
    self.la_email = Label(master, text='Email:', font=('arial 9 bold'))
    self.la_email.place(x=30, y=129)

    self.e_tel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_tel.place(x=430, y=100)
    self.la_tel = Label(master, text='Telefone:', font=('arial 9 bold'))
    self.la_tel.place(x=430, y=69)

    self.e_cel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_cel.place(x=620, y=100)
    self.la_cel = Label(master, text='Celular:', font=('arial 9 bold'))
    self.la_cel.place(x=620, y=69)

    self.e_produto = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_produto.place(x=430, y=150)
    self.la_produto = Label(master, text='Produtos:', font=('arial 9 bold'))
    self.la_produto.place(x=430, y=129)

    self.salvar = Button(master, text='Salvar', bg='#f17215',
                         bd=2, relief='raise', width=15, height=2, command=self.add_fornecedores)
    self.salvar.place(x=220, y=700)
    self.atualiza = Button(master, text='Atualizar', bg='#f17215',
                           bd=2, relief='raise', width=15, height=2)  # , command=self.atualizar)
    self.atualiza.place(x=360, y=700)
    self.limpar = Button(master, text='Novo', bg='#f17215',
                         bd=2, relief='raise', width=15, height=2, command=self.clear)
    self.limpar.place(x=500, y=700)
    self.deletar = Button(master, text='Deletar', bg='#f17215',
                          bd=2, relief='raise', width=15, height=2)  # , command=self.delete)
    self.deletar.place(x=640, y=700)

    self.tree = ttk.Treeview(master, height=22, selectmode='browse')
    self.tree["columns"] = ["#1", "#2", "#3", "#4", "#5"]
    self.tree.bind('<<TreeviewSelect>>', self.entry_tree)
    self.tree.place(x=30, y=200)
    self.tree.column("#0", stretch=False, width=120)
    self.tree.column("#1", stretch=False, width=150)
    self.tree.column("#2", stretch=False, width=150)
    self.tree.column("#3", stretch=False, width=150)
    self.tree.column("#4", stretch=False, width=150)
    self.tree.column("#5", stretch=False, width=200)

    self.tree.heading("#0", text="Código")
    self.tree.heading("#1", text="Fornedor")
    self.tree.heading("#2", text="Telefone")
    self.tree.heading("#3", text="Celular")
    self.tree.heading("#4", text="Email")
    self.tree.heading("#5", text="Produtos")
    self.get_fornecedores()

    self.xss = ttk.Scrollbar(orient=HORIZONTAL)
    self.xss.configure(command=self.tree.xview)
    self.tree.configure(xscrollcommand=self.xss.set)
    self.tree.insert("", END)
    self.xss.place(x=30, y=670, width=925)

    self.yss = ttk.Scrollbar(orient=VERTICAL)
    self.yss.configure(command=self.tree.yview)
    self.tree.configure(yscrollcommand=self.yss.set)
    self.tree.insert("", END)
    self.yss.place(x=955, y=200, height=485)

  def view_registros(self):
    return c.execute("SELECT id, * FROM forneced")

  def get_fornecedores(self, *args, **kwargs):
    record = self.tree.get_children()
    for element in record:
      self.tree.delete(element)
    sql = "SELECT * FROM forneced ORDER BY fornecedor DESC"
    c.execute(sql)
    for row in self.view_registros():
      self.tree.insert('', 'end', text=row[1],
                       values=(row[2], row[3], row[4], row[5], row[6]))

  def entry_tree(self, *args, **kwargs):
    print(self.tree.selection())

    fornecedor = self.tree.item(self.tree.selection())["values"][0]
    tel = self.tree.item(self.tree.selection())["values"][1]
    cel = self.tree.item(self.tree.selection())["values"][2]
    email = self.tree.item(self.tree.selection())["values"][3]
    produto = self.tree.item(self.tree.selection())["values"][4]

    self.e_fornecedor.delete(0, END)
    self.e_fornecedor.insert(END, str(fornecedor))
    self.e_tel.delete(0, END)
    self.e_tel.insert(END, str(tel))
    self.e_cel.delete(0, END)
    self.e_cel.insert(END, str(cel))
    self.e_email.delete(0, END)
    self.e_email.insert(END, str(email))
    self.e_produto.delete(0, END)
    self.e_produto.insert(END, str(produto))

  def add_fornecedores(self, *args, **kwargs):
    self.fornecedor = self.e_fornecedor.get()
    self.email = self.e_email.get()
    self.tel = self.e_tel.get()
    self.cel = self.e_cel.get()
    self.produto = self.e_produto.get()

    if self.e_fornecedor == "" or self.e_email == "" or self.e_cel == "" or self.e_produto == "":
      messagebox.showinfo(' Barber Shop', 'CAMPO OBRIGATÓRIO!')

    else:
      sql = "INSERT INTO forneced(fornecedor, email, telefone, celular, produto)VALUES(?,?,?,?,?)"
      c.execute(sql, (self.fornecedor, self.tel, self.cel, self.email, self.produto))
      conn.commit()
      messagebox.showinfo('Barber Shop', 'CADASTRO RALIZADO COM SUCESSO!')
      self.get_fornecedores()

  def clear(self, *args, **kwargs):
    self.e_fornecedor.delete(0, END)
    self.e_tel.delete(0, END)
    self.e_cel.delete(0, END)
    self.e_email.delete(0, END)
    self.e_produto.delete(0, END)

  def atualizar(self, *args, **Kwargs):
    self.up_1 = self.e_fornecedor.get()
    self.up_2 = self.e_tel.get()
    self.up_3 = self.e_cel.get()
    self.up_4 = self.e_email.get()
    self.up_5 = self.e_produto.get()

    query = "UPDATE forneced SET fornecedor=? ,email=?, telefone=?, celular=?, produto=? "
    c.execute(query, (self.up_1, self.up_2, self.up_3, self.up_4, self.up_5))
    conn.commit()
    messagebox.showinfo('SISTEMA DE VENDAS', 'ATUALIZAÇAO REALIZADA COM SUCESSO!')

  def delete(self, *args, **kwargs):
    c.execute('DELETE FROM forneced WHERE id = ?', (id,))
    conn.commit()
    self.tree.delete()
    messagebox.showinfo('Barber Shop', 'CLIENTE APAGADO COM SUCESSO!')


janela = Tk()
main = Fornecedor(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0, 0)
janela.config()
janela.title()

janela.mainloop()
