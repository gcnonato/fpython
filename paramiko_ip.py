#!/usr/bin/python
# import os
# import paramiko
# from getpass import getpass
# enderecos = arquivo contendo endereços IP
# routers = open("enderecos")
# COLETAR AS CREDENCIAIS
user = "usuario"
passw = "senha"

routers = ['127.0.0.1', '201.42.148.239', '10.234.434.12']

for ip in routers:
    print("Verify ICMP Status IP: "+ip+"...")
    resposta = 0  # os.system("ping -c 5 " + ip + "> /dev/null")
    if resposta == 0:
        print(ip+" - Status ICMP OK")
        print("Running backup process - "+ip)
        # ssh_client = paramiko.SSHClient()
        # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh_client.connect(hostname=ip,port=2222,username=user,password=passw)
        # stdin,stdout,stderr = ssh_client.exec_command("export terse\n")
        # print(stdout.read())
        # ler_config = stdout.read()
        # ler_config = "127.0.0.1"
        filename = f'backup-{ip}.txt'
        with open(filename, "w") as arquivo:
            arquivo.write(ip)
    else:
        print(ip+" - Status ICMP PROBLEM")
