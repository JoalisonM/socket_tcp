from socket import *

serverHost = "localhost"
serverPort = 50007

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverHost, serverPort))

mensagem = input("Usuário do github: ")
sock.sendall(mensagem.encode("utf-8"))

data = sock.recv(4096)
print("Repositórios de %s: %s"%(mensagem, data.decode()))

sock.close()