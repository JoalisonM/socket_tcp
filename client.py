"""
Autores: 
Joalison Matheus da Silva Ferreira e 
Matheus Soares de Sales
"""

from socket import *

serverHost = "localhost"
serverPort = 50007

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverHost, serverPort))

mensage = input("Usuário do github: ")
sock.sendall(mensage.encode("utf-8"))

data = sock.recv(4096)
print("Repositórios de %s: %s"%(mensage, data.decode()))

sock.close()