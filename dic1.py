#iterando as chaves e valores de uma lista

valores={
    'chave':[1,2,3,4,5],
    'chave0':[1,2,3,4,5],
    'chave1':["a","b","c","d","e"]
}
#loop for armazena rspectivamente as chaves e seus valores nas variaveis "chaves" e "valor" 
#sendo que as chaves e valores são extraidas do dicionario pela função "itens()"em formato de pares de tuplas
#e por fim printa na tela o resultado ate que todas as chaves e valores sejam armazenadas e printadas
for chave, valor in valores.items():
    print(f"chave {chave}, valor {valor}")

#usando a função print para imprimir rusticamente todas as chaves e valores do dicionario
print(valores.items())