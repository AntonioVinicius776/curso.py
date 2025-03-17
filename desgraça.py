import pandas as pd
import matplotlib.pyplot as pit

dxp=pd.read_csv('thats my name.csv',delimiter=',')
pit.figure(figsize=(10,6))

for produto in dxp['produto'].unique():
    dxp=dxp[dxp['produto']==produto]
    pit.plot(dxp['ano'], dxp['preco'], marker='o')

pit.title("aos anos")
pit.xlabel('ano')
pit.ylabel('preco')
pit.legend(title='produto')

pit.grid(True)
pit.show()