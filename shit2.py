import pandas as pd
pol = pd.read_csv("agoravai.csv")
print(pol)

pol["preco"].max()
print("confia",pol["preco"].mean())