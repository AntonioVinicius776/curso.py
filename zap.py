import time
import random

usermen=[]
fra=str(input("deseja inserir uma frase "))
while fra == "s" :
    usermen.append(input())
    fra=str(input("ainda deseja inserir uma frase "))

print(usermen)