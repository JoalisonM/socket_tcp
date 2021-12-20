"""
Autores: 
Joalison Matheus da Silva Ferreira e 
Matheus Soares de Sales
"""

import json
import requests
from socket import *

def githubReps(user):
  answer = requests.get(f"https://api.github.com/users/{user}/repos")
  reps = []

  if answer.status_code == 200:
    dataJson = answer.json()
    if type(dataJson) is not int:
      for i in range(len(dataJson)):
        reps.append({
          "nome": dataJson[i]["name"],
          "html_url": dataJson[i]["html_url"],
        })

  repsString = json.dumps(reps, indent=4, sort_keys=True, default=str)
  return repsString

HOST = ""
PORT = 50007

sock = socket(AF_INET, SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(1)

while True:
  connection, address = sock.accept()
  print("Server conectado por", address, "\n")

  while True:
    data = connection.recv(4096)

    if not data: break

    message = githubReps(data.decode())

    connection.sendall(message.encode("utf-8"))

  connection.close()