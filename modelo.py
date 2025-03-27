import pandas as pd

# Ler o arquivo CSV existente (se houver)
df_existing = pd.read_csv('addtocsv.csv')

# Criar um novo DataFrame com os dados que você deseja adicionar
novos_dados = {
    'coluna1': ['valor1', 'valor2'],
    'coluna2': ['valor3', 'valor4'],
    # Adicione mais colunas e valores conforme necessário
}
df_novos_dados = pd.DataFrame(novos_dados)

# Concatenar o DataFrame existente com o novo DataFrame
df_combined = pd.concat([df_existing, df_novos_dados], ignore_index=True)

# Salvar o DataFrame resultante de volta no arquivo CSV
df_combined.to_csv('novo.csv', index=False)