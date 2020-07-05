import sqlite3
from subprocess import *
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect('C:\sistema_salao\DataBase\my_database.db')
c = conn.cursor()
result = c.execute('SELECT MAX (id) from product')
for r in result:
  id = r[0]


class Produtos:
  def __init__(self, master, *args, **kw):
    self.master = master

    self.frame1 = Frame(master, width=1000, height=50,
                        bg='#222125', bd=1, relief='raise')
    self.frame1.pack(side=TOP)
    self.frame2 = Frame(master, width=1000, height=50,
                        bg='#222125', bd=1, relief='raise')
    self.frame2.pack(side=BOTTOM)

    self.label1 = Label(self.frame1, text='Nova Venda', font='arial 25 bold', bg="#222125", fg='white')
    self.label1.place(x=400, y=0)

    self.add = Button(master, text='Add', bg='#f17215',
                      bd=2, relief='raise', width=18, height=3)  # , command=self.delete)
    self.add.place(x=500, y=700)

    self.limpar = Button(master, text='Limpar', bg='#f17215',
                         bd=2, relief='raise', width=18, height=3)  # , command=self.delete)
    self.limpar.place(x=320, y=700)

    self.tree = ttk.Treeview(master, selectmode='browse', height=29)
    self.tree["columns"] = ["#1", "#2", "#3", "#4", "#5", "#6", "#7"]
    self.tree.bind('<<TreeviewSelect>>', self.entry_tree)
    self.tree.place(x=20, y=70)
    self.tree.column("#0", stretch=False, width=100)
    self.tree.column("#1", stretch=False, width=120)
    self.tree.column("#2", stretch=False, width=128)
    self.tree.column("#3", stretch=False, width=128)
    self.tree.column("#4", stretch=False, width=120)
    self.tree.column("#5", stretch=False, width=120)
    self.tree.column("#6", stretch=False, width=120)
    self.tree.column("#7", stretch=False, width=120)
    self.tree.heading("#0", text="Código")
    self.tree.heading("#1", text="Produto")
    self.tree.heading("#2", text="Fornecedor")
    self.tree.heading("#3", text="Preço de Custo")
    self.tree.heading("#4", text="Preço de Venda")
    self.tree.heading("#5", text="Estoque")
    self.tree.heading("#6", text="Lote")
    self.tree.heading("#7", text="Vencimento")
    self.get_produtos()

    self.xss = ttk.Scrollbar(orient=HORIZONTAL)
    self.xss.configure(command=self.tree.xview)
    self.tree.configure(xscrollcommand=self.xss.set)
    self.tree.insert("", 0, END)
    self.xss.place(x=20, y=678, width=960)

    self.yss = ttk.Scrollbar(orient=VERTICAL)
    self.yss.configure(command=self.tree.yview)
    self.tree.configure(yscrollcommand=self.yss.set)
    self.tree.insert("", END, 0)
    self.yss.place(x=980, y=70, height=605)

  def view_registros(self):
    return c.execute("SELECT id, * FROM product")

  def get_produtos(self, *args, **kwargs):
    record = self.tree.get_children()
    for element in record:
      self.tree.delete(element)
    sql = "SELECT * FROM product ORDER BY produto DESC"
    c.execute(sql)
    for row in self.view_registros():
      self.tree.insert('', 'end', text=row[1],
                       values=(row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

  def entry_tree(self, *args, **kwargs):
    valor = self.e_vup(check_call('./self.e_vup'))

    print(self.tree.selection())

    produto = self.tree.item(self.tree.selection())["values"][0]
    fornecedor = self.tree.item(self.tree.selection())["values"][1]
    vlr_custo = self.tree.item(self.tree.selection())["values"][2]
    vlr_venda = self.tree.item(self.tree.selection())["values"][3]
    estoque = self.tree.item(self.tree.selection())["values"][4]
    lote = self.tree.item(self.tree.selection())["values"][5]
    vencimento = self.tree.item(self.tree.selection())["values"][6]

    self.e_vup.delete(0, END)
    self.e_vup.insert(END, str(vlr_custo))

    '''#self.e_fornecedor.delete(0, END)
    self.e_fornecedor.insert(END, str(fornecedor))
    self.e_vlr_custo.delete(0, END)
    self.e_vlr_custo.insert(END, str(vlr_custo))
    self.e_vlr_venda.delete(0, END)
    self.e_vlr_venda.insert(END, str(vlr_venda))
    self.e_estoque.delete(0, END)
    self.e_estoque.insert(END, str(estoque))
    self.e_lote.delete(0, END)
    self.e_lote.insert(END, str(lote))
    self.e_vencimento.delete(0, END)
    self.e_vencimento.insert(END, str(vencimento))




def atualizar(self, *args, **Kwargs):
    self.up_1 = self.e_produto.get()
    self.up_2 = self.e_vlr_custo.get()
    self.up_3 = self.e_vlr_venda.get()
    self.up_4 = self.e_estoque.get()



    query = "UPDATE product SET produto=?, vlr_custo=?, vlr_venda=? WHERE estoque=?"
    c.execute(query, (self.up_1, self.up_2, self.up_3, self.up_4, ))
    conn.commit()
    messagebox.showinfo('SISTEMA DE VENDAS', 'ATUALIZAÇAO REALIZADA COM SUCESSO!')

def delete(self, *args, **kwargs):
    c.execute('DELETE FROM product WHERE id = ?', (id,) )
    conn.commit()
    self.tree.delete()
    messagebox.showinfo('Barber Shop', 'PRODUTO APAGADO COM SUCESSO!')#'''


janela = Tk()
main = Produtos(janela)
janela.geometry('1000x825+300+0')
janela.resizable(0, 0)
janela.config()
janela.title()

janela.mainloop()
