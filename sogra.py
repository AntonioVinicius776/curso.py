#crie um programa que envie mensagens personalizadas a uma lista de nomes: o script deve
#1 pedir ao usuario uma lista de nomes
#2 criar uma mensagem personalizada
#3 exibir a mensagem com um pequeno intervalo entre os envios (simulando um chatbot)

import random
import time

contatos=["eu", "tu", "nois", "bota", "nelas"]

user=str(input("qual o usuario \n"))

for contato in contatos:
    if contato==user:
        print(f"bem vindo {user}")
    else:
        print("usuario invalido")