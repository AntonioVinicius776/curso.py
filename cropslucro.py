import pandas as pd
import matplotlib.pyplot as pit

tab=pd.read_csv('stardew valley0.csv',delimiter=',')
pit.figure(figsize=(10,5))

for crop in tab['crops'].unique():
    pit.plot(tab['crops'],tab['produtividade'],label=crop,marker='o')

pit.title("produção ao longo dos anos")
pit.xlabel('ano')
pit.ylabel('preço')
pit.legend(title='crops')

pit.grid(True)
pit.show()