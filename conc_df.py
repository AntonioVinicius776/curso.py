import pandas as pd

oldates = {
    'peixes':['tambaki','matrinxa','jaraki'],
    'valor/kg':[10,8,5],
    'custo/kg':[4,5,2]
}
oldf = pd.DataFrame(oldates)

newdates={
    'produção/kg':[800,750,200]
    }

newdf=pd.DataFrame(newdates)

concdf=pd.concat([oldf,newdf],ignore_index=True)

concdf.to_csv('concatenado.csv',index=False)

concatenado=pd.read_csv('concatenado.csv', delimiter=',')

print(oldf)
print(newdf)
print(concdf)
print(concatenado)