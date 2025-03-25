import matplotlib.pyplot as plt #importando a biblioteca de visualização grafica

#estilo do grafico
plt.style.use('Solarize_Light2')

#lista de dados a serem exibidos
x=[1,2,3]
max=[7,8,10]
min=[4,5,6]

#rotulo do eixo x
plt.xlabel("x")
#rotuko do eixo y
plt.ylabel("y")

#plotando no grafico os dados das listas x e y respectivamente
plt.plot(x,max,linestyle='--',color='r',marker='o')#especificações sobre os detalhes visuais das linhas
plt.plot(x,min,marker='o')

#referenciando as linhas do grafico na ordem em que foram plotadas
plt.legend(["max","min"])
#colocando grade no grafico
plt.grid(True)
#executando/mostrando o grafico
plt.show()