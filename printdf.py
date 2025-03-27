import pandas as pd

Fdates={
    'peixes':['tambaki','matrinxa','jaraki'],
    'valor/kg':[10,8,5],
    'custo/kg':[4,5,2],
    'produção/kg':[800,750,200]
    }

fishtab=pd.DataFrame(Fdates)

print(fishtab)