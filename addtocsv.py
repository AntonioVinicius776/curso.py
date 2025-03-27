import pandas as pd

newFdates={
    'peixes':['tambaki','matrinxa','jaraki'],
    'valor/kg':[10,8,5],
    'custo/kg':[4,5,2],
    'produção/kg':['muito','meio','pouco']
    }

fishtab=pd.DataFrame(newFdates)

fishtab.to_csv('',index=False)

tab=pd.read_csv('',delimiter=',')

print(tab)