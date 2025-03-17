import pandas as din
pol = din.read_csv("agoravai.csv")

allval=pol["preco"].idxmax()
car=pol.loc[allval,"produto"]
val=pol.loc[allval,"preco"]

print("mais caro ", car, "com", val,"unidedes")