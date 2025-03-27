#teste de acesso e de operação com valores em um dicionario

#dicionario com listas no valor da chave
valores={
    'chave':[1,2,3,4,5],
    'chave0':[1,2,3,4,5],
    'chave1':["a","b","c","d","e"]
}
#função get() que extrai todos os valores de uma chave existente esta sendo armazenada na var 'osvalores' para uso posterior
#(e caso não exista retorna um valor padrão definido e none se nada for definido)
osvalores=valores.get('chave','NOOOSSAAA')

#armazenando em uma variavel um item de uma lista armazenada em uma chave do dicionario valores
n=valores['chave'][1]
n0=valores['chave0'][2]

#imprimindo os resultados
print(osvalores)
print(n+n0) 

#nice