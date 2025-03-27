import pandas as pd
import matplotlib.pyplot as pit

tab=pd.read_csv('idh0.csv',delimiter=',')
pit.figure(figsize=(10,5))


pit.plot(tab['Year'],tab['idh'],marker='o')



pit.title("produção ao longo dos anos")
#pit.xlabel('ano')
#pit.ylabel('preço')
#pit.legend(title='crops')

pit.grid(True)
pit.show()