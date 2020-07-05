import os
from ftplib import FTP
from time import sleep

import environ

environ.Path(__file__)
env = environ.Env()
env.read_env(".envs/.env")


def conectar(conectar_a_conta):

    if conectar_a_conta == "luciano":
        print(env("HOST_LUCIANO"), env("USER_LUCIANO"), env("PASSWORD_LUCIANO"))
        return FTP(env("HOST_LUCIANO"), env("USER_LUCIANO"), env("PASSWORD_LUCIANO"))
    else:
        print(env("HOST_FABRIZIO"), env("USER_FABRIZIO"), env("PASSWORD_FABRIZIO"))
        return FTP(env("HOST_FABRIZIO"), env("USER_FABRIZIO"), env("PASSWORD_FABRIZIO"))


# ftp.dir('public_html')


def listar(self):
    self.cwd("public_html")
    self.retrlines("LIST")


def download(self, file=None):
    self.retrbinary("RETR {}".format(file), open(file, "wb").write)
    apagar = input(
        u"{} \n Deletar o arquivo {} (S)im - (N)ão?.: ".format("*" * 60, file)
    )
    msg = "Arquivo não Apagado!"
    if apagar == "s" or apagar == "s".upper():
        self.delete(file)
        msg = "Arquivo Apagado!"
    self.quit()
    return msg


def delete(self):
    self.cwd("public_html")
    self.retrlines("LIST")
    arquivo = input("Nome do arquivo que será apagado.: ")
    apagar = input(
        u"{} \n Deletar o arquivo? {} (S)im - (N)ão?.: ".format("*" * 60, arquivo)
    )
    msg = "Arquivo não Apagado!"
    if apagar == "s" or apagar == "s".upper():
        self.delete(arquivo)
        msg = "Arquivo Apagado!"
    self.retrlines("LIST")
    self.quit()


def upload(self):
    self.cwd("public_html")
    self.retrlines("LIST")
    arquivo = input("Nome do arquivo para upload.: ")
    subir = input(
        u"{} \n Upload do arquivo? {} (S)im - (N)ão?.: ".format("*" * 60, arquivo)
    )
    msg = "Arquivo não Upado!"
    if subir == "s" or subir == "s".upper():
        self.storbinary("STOR {}".format(arquivo), open(arquivo, "rb"))
        msg = "Arquivo Upado!"
    self.retrlines("LIST")
    self.quit()


def ftps(submenu):
    if submenu == "1":
        connection = conectar("fabrizio")
        listar(connection)
        baixar = input("Fazer download?(S)im/(N)ão.: ")
        if baixar == "s" or baixar == "s".upper():
            nome = input("Nome do arquivo.: ")
            print(download(connection, nome))
    elif submenu == "2":
        listar(conectar("luciano"))
        baixar = input("Fazer download?(S)im/(N)ão.: ")
        if baixar == "s" or baixar == "s".upper():
            nome = input("Nome do arquivo.: ")
            # print(download(connection, nome))
    elif submenu == "3":
        conexao = input("Conectar em?(F)abrizio/(L)uciano.: ")
        if conexao == "f" or conexao == "f".upper():
            connection = conectar("fabrizio")
        else:
            connection = conectar("luciano")
        delete(connection)
        listar(connection)
    elif submenu == "5":
        conexao = input("Conectar em?(F)abrizio/(L)uciano.: ")
        if conexao == "f" or conexao == "f".upper():
            connection = conectar("fabrizio")
        else:
            connection = conectar("luciano")
        upload(connection)
        listar(connection)
    elif submenu == "4":
        print("Saindo...")
        print("")
        sleep(0.3)  # Time in seconds.
        submenu = "4"
    else:
        print("Esta não é uma opção válida!")
        sleep(0.5)  # Time in seconds.
    return submenu


def menu():
    os.system("cls")
    print(u"\nQual FTP conectar?\n")
    print("(1) FABRIZIO\n")
    print("(2) LUCIANO\n")
    print("(3) DELETAR\n")
    print("(5) UPLOAD\n")
    print("(4) Sair do Script FTP\n")
    submenu = input("Escolha uma das opções acima..:")
    return ftps(submenu)


def main():

    submenu = ""
    while submenu != "4":
        submenu = menu()


main()
# for a in os.environ:
# 	print('Var: ', a, 'Value: ', os.getenv(a))
