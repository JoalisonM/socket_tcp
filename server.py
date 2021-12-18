import json
import requests
from socket import *

def githubReps(usuario):
  resposta = requests.get(f"https://api.github.com/users/{usuario}/repos")
  reps = []

  if resposta.status_code == 200:
    dados = resposta.json()
    if type(dados) is not int:
      for i in range(len(dados)):
        reps.append({
          "nome": dados[i]["name"],
          "html_url": dados[i]["html_url"],
        })

  repsString = json.dumps(reps, indent=4, sort_keys=True, default=str)
  return repsString

HOST = ""
PORT = 50007

sock = socket(AF_INET, SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(5)

while True:
  conexao, endereco = sock.accept()
  print("Server conectado por", endereco, "\n")

  while True:
    data = conexao.recv(4096)

    if not data: break

    mensagem = githubReps(data.decode())

    conexao.sendall(mensagem.encode("utf-8"))

  conexao.close()