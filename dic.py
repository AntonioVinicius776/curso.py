dic={
    "nome": ["melancia", "manga", "panana"],
    "quantidade": [1, 2, 3],
    "preço": [100, 10000, 100000]
}
for nome, quantidade, preço in zip(dic["nome"], dic["quantidade"], dic["preço"]):
        print("produto:", nome, "quantidade:", quantidade, "preço", preço)

        dic["preço"]=1

for chave, valor in dic.items():
    print(chave, valor)
    
chaves=dic.keys()
valores=dic.values()

print(chaves)
print(valores)

#eu quero pagar impooooossstoooooo