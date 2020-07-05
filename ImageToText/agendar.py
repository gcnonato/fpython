from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import connection


class Agenda:
  conn = None

  def __init__(self, master):
    self.conn = connection.Dao()

    self.master = master

    self.frame1 = Frame(master, width=1000, height=25,
                        bg='#222125', bd=1, relief='raise')
    self.frame1.pack(side=TOP)

    self.frame2 = Frame(master, width=1000, height=25,
                        bg='#222125', bd=1, relief='raise')
    self.frame2.pack(side=BOTTOM)

    self.label1 = Label(self.frame1, text='Agendamento', font='arial 15 bold',
                        bg='#222125', fg='white')
    self.label1.place(x=385, y=0)

    self.e_id = Entry(master, width=10, font=('arial 10 bold'), bd=1, relief="solid")
    self.e_id.place(x=50, y=45)
    self.la_id = Label(master, text='ID:', font=('arial 9 bold'))
    self.la_id.place(x=30, y=45)

    self.e_cliente = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_cliente.place(x=30, y=100)
    self.la_cliente = Label(master, text='Cliente:', font=('arial 9 bold'))
    self.la_cliente.place(x=30, y=69)

    self.e_email = Entry(master, width=40, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_email.place(x=420, y=100)
    self.la_email = Label(master, text='Email:', font=('arial 9 bold'))
    self.la_email.place(x=420, y=69)

    self.e_tel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_tel.place(x=810, y=100)
    self.la_tel = Label(master, text='Telefone:', font=('arial 9 bold'))
    self.la_tel.place(x=810, y=69)

    self.e_cel = Entry(master, width=15, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_cel.place(x=810, y=150)
    self.la_cel = Label(master, text='Celular:', font=('arial 9 bold'))
    self.la_cel.place(x=810, y=129)

    self.e_func = Entry(master, width=25, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_func.place(x=30, y=150)
    self.la_func = Label(master, text='Funcionário:', font=('arial 9 bold'))
    self.la_func.place(x=30, y=129)

    self.e_serv = Entry(master, width=25, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_serv.place(x=300, y=150)
    self.la_serv = Label(master, text='Serviço:', font=('arial 9 bold'))
    self.la_serv.place(x=300, y=129)

    self.e_hora = Entry(master, width=10, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_hora.place(x=560, y=150)
    self.la_hora = Label(master, text='Horário:', font=('arial 9 bold'))
    self.la_hora.place(x=560, y=129)

    self.e_data = Entry(master, width=10, font=('arial 12 bold'), bd=1, relief="solid")
    self.e_data.place(x=690, y=150)
    self.la_data = Label(master, text='Data:', font=('arial 9 bold'))
    self.la_data.place(x=690, y=129)

    self.salvar = Button(master, text='Salvar', bg='#f17215',
                         bd=2, relief='raise', width=15, height=2, command=self.add_cliente)  # and self.up_tree)
    self.salvar.place(x=200, y=725)
    self.clear = Button(master, text='Novo', bg='#f17215',
                        bd=2, relief='raise', width=15, height=2, command=self.clear)
    self.clear.place(x=350, y=725)

    self.atualiza = Button(master, text='Atualizar', bg='#f17215',
                           bd=2, relief='raise', width=15, height=2, command=self.atualizar)
    self.atualiza.place(x=500, y=725)
    self.deletar = Button(master, text='Deletar', bg='#f17215',
                          bd=2, relief='raise', width=15, height=2, command=self.delete)
    self.deletar.place(x=650, y=725)

    self.tree = ttk.Treeview(master, height=23, selectmode='browse')
    self.tree["columns"] = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"]
    self.tree.bind('<<TreeviewSelect>>', self.entry_tree)
    self.tree.place(x=30, y=200)
    self.tree.column("#0", stretch=False, width=90)
    self.tree.column("#1", stretch=False, width=100)
    self.tree.column("#2", stretch=False, width=100)
    self.tree.column("#3", stretch=False, width=100)
    self.tree.column("#4", stretch=False, width=150)
    self.tree.column("#5", stretch=False, width=100)
    self.tree.column("#6", stretch=False, width=100)
    self.tree.column("#7", stretch=False, width=100)
    self.tree.column("#8", stretch=False, width=100)
    self.tree.heading("#0", text="Código")
    self.tree.heading("#1", text="Nome")
    self.tree.heading("#2", text="Telefone")
    self.tree.heading("#3", text="Celular")
    self.tree.heading("#4", text="Email")
    self.tree.heading("#5", text="Funcionário")
    self.tree.heading("#6", text="Serviço")
    self.tree.heading("#7", text="Hora")
    self.tree.heading("#8", text="Data")
    self.get_client()

    self.xss = ttk.Scrollbar(orient=HORIZONTAL)
    self.xss.configure(command=self.tree.xview)
    self.tree.configure(xscrollcommand=self.xss.set)
    self.tree.insert("", END)
    self.xss.place(x=30, y=690, width=945)

    self.yss = ttk.Scrollbar(orient=VERTICAL)
    self.yss.configure(command=self.tree.yview)
    self.tree.configure(yscrollcommand=self.yss.set)
    self.tree.insert("", END)
    self.yss.place(x=975, y=200, height=505)

  def view_registros(self, *args, **kwargs):
    return self.conn.getCursor().execute("SELECT id, * FROM agend")

  def get_client(self, *args, **kwargs):
    record = self.tree.get_children()
    for element in record:
      self.tree.delete(element)
    sql = "SELECT * FROM agend ORDER BY nome DESC"
    self.conn.getCursor().execute(sql)
    for row in self.view_registros():
      self.tree.insert('', 'end', text=row[1],
                       values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

  def add_cliente(self, *args, **kwargs):
    self.cliente = self.e_cliente.get()
    self.tel = self.e_tel.get()
    self.cel = self.e_cel.get()
    self.email = self.e_email.get()
    self.func = self.e_func.get()
    self.serv = self.e_serv.get()
    self.hora = self.e_hora.get()
    self.data = self.e_data.get()

    if self.e_cliente == "" or self.e_cel == "" or self.e_serv == "" or self.e_hora == "" or self.e_data == "":
      messagebox.showinfo(' Barber Shop', 'CAMPO OBRIGATÓRIO!')

    else:
      sql = "INSERT INTO agend(Nome, Telefone, Celular, Email, Funcionario, Serviço, Hora, Data)VALUES (?,?,?,?,?,?,?,?) "
      self.conn.getCursor().execute(sql, (
      self.cliente, self.tel, self.cel, self.email, self.func, self.serv, self.hora, self.data))
      self.conn.getConn().commit()
      messagebox.showinfo('Barber Shop', 'CADASTRO RALIZADO COM SUCESSO!')
    self.get_client()

  def clear(self, *args, **kwargs):
    self.e_id.delete(0, END)
    self.e_cliente.delete(0, END)
    self.e_tel.delete(0, END)
    self.e_cel.delete(0, END)
    self.e_email.delete(0, END)
    self.e_func.delete(0, END)
    self.e_serv.delete(0, END)
    self.e_hora.delete(0, END)
    self.e_data.delete(0, END)

    listar = self.conn.listar()
    if listar.rowcount > 0:
      for r in self.conn.listar():
        # self.id = r[0]
        self.nome = r[1]
        self.telefone = r[2]
        self.celular = r[3]
        self.email = r[4]
        self.funcionario = r[5]
        self.servico = r[6]
        self.hora = r[7]
        self.data = r[8]

    self.conn.getConn().commit()
    self.e_id.delete(0, END)
    self.e_id.insert(0, str(self.id))
    self.e_cliente.delete(0, END)
    self.e_cliente.insert(0, str(self.nome))
    self.e_tel.delete(0, END)
    self.e_tel.insert(0, str(self.telefone))
    self.e_cel.delete(0, END)
    self.e_cel.insert(0, str(self.celular))
    self.e_email.delete(0, END)
    self.e_email.insert(0, str(self.email))
    self.e_func.delete(0, END)
    self.e_func.insert(0, str(self.funcionario))
    self.e_serv.delete(0, END)
    self.e_serv.insert(0, str(self.servico))
    self.e_hora.delete(0, END)
    self.e_hora.insert(0, str(self.hora))
    self.e_data.delete(0, END)
    self.e_data.insert(0, str(self.data))

  def entry_tree(self, *args, **kwargs):
    print(self.tree.selection())

    id = self.tree.item(self.tree.selection())["values"][0]
    nome = self.tree.item(self.tree.selection())["values"][1]
    tel = self.tree.item(self.tree.selection())["values"][2]
    cel = self.tree.item(self.tree.selection())["values"][3]
    email = self.tree.item(self.tree.selection())["values"][4]
    func = self.tree.item(self.tree.selection())["values"][5]
    serv = self.tree.item(self.tree.selection())["values"][6]
    hora = self.tree.item(self.tree.selection())["values"][7]
    data = self.tree.item(self.tree.selection())["values"][8]

    self.e_id.delete(0, END)
    self.e_id.insert(END, str(id))
    self.e_cliente.delete(0, END)
    self.e_cliente.insert(END, str(nome))
    self.e_tel.delete(0, END)
    self.e_tel.insert(END, str(tel))
    self.e_cel.delete(0, END)
    self.e_cel.insert(END, str(cel))
    self.e_email.delete(0, END)
    self.e_email.insert(END, str(email))
    self.e_func.delete(0, END)
    self.e_func.insert(END, str(func))
    self.e_serv.delete(0, END)
    self.e_serv.insert(END, str(serv))
    self.e_hora.delete(0, END)
    self.e_hora.insert(END, str(hora))
    self.e_data.delete(0, END)
    self.e_data.insert(END, str(data))

  def atualizar(self, *args, **kwargs):
    self.up_0 = self.e_id.get()
    self.up_1 = self.e_cliente.get()
    self.up_2 = self.e_tel.get()
    self.up_3 = self.e_cel.get()
    self.up_4 = self.e_email.get()
    self.up_5 = self.e_func.get()
    self.up_6 = self.e_serv.get()
    self.up_7 = self.e_hora.get()
    self.up_8 = self.e_data.get()
    sql = "UPDATE agend SET nome=?, telefone=?, celular=?, email=?, funcionario=?, serviço=?, hora=?, data=?" \
          "WHERE id=?"
    self.conn.getCursor().execute(sql,
                                  (self.up_1, self.up_2, self.up_3, self.up_4, self.up_5, self.up_6, self.up_7,
                                   self.up_8, self.up_0)
                                  )
    self.conn.getConn().commit()
    messagebox.showinfo('SISTEMA DE VENDAS', 'ATUALIZAÇAO REALIZADA COM SUCESSO!')
    self.get_client()

  def delete(self, *args, **kwargs):
    """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
    """
    id = self.e_id.get()
    sql = 'DELETE FROM agend WHERE id = ?'
    print(id)
    self.conn.getCursor().execute(sql, (id,))
    # self.conn.getConn().commit()
    self.tree.item(self.tree.selection())
    messagebox.showinfo('Barber Shop', 'CLIENTE APAGADO COM SUCESSO!')
    self.get_client()


janela = Tk()
main = Agenda(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0, 0)
janela.config()
janela.title()

janela.mainloop()
