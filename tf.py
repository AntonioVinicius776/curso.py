#Gráfico 1: Relação entre IDH e Taxa de Fecundidade → 
# Mostra que países com maior IDH tendem a ter uma taxa de fecundidade menor.

#importando uma biblioteca de visualização grafica
import matplotlib.pyplot as plt
#importando uma biblioteca de manipulação de dados
import pandas as pd

plt.style.use('Solarize_Light2')

tf=pd.read_csv('dados0.csv',delimiter=';')
plt.figure(figsize=(10,5))

plt.plot(tf['ano'],tf['fertilidademb'],label='brasil',marker='o')
plt.plot(tf['ano'],tf['fertilidademlb'],label='luxemburgo',marker='o')
plt.plot(tf['ano'],tf['fertilidademfp'],label='filipinas',marker='o')
plt.plot(tf['ano'],tf['fertilidademus'],label='estados unidos',marker='o')
plt.plot(tf['ano'],tf['fertilidademm'],label='global',marker='o')

plt.xlabel('ano')
plt.ylabel('taxa de fecundidade')

plt.xlim(1999,2025)
#plt.ylim(0,5)

plt.title('Taxa de fecundidade ao decorrer dos anos')
plt.grid(True)
plt.legend(title='Taxa de fecundidade')
plt.show()