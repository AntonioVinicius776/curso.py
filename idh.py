#importando uma biblioteca de visualização grafica
import matplotlib.pyplot as plt
#importando uma biblioteca de manipulação de dados
import pandas as pd

tf=pd.read_csv('idh0.csv',delimiter=';')
plt.figure(figsize=(10,5))

plt.plot(tf['year'],tf['idhbr'],label='brasil',marker='o')
plt.plot(tf['year'],tf['idhlux'],label='luxemburgo',marker='o')
plt.plot(tf['year'],tf['idhphl'],label='filipinas',marker='o')
plt.plot(tf['year'],tf['usa'],label='estados unidos',marker='o')
plt.plot(tf['year'],tf['idhw'],label='global',marker='o')

plt.show()