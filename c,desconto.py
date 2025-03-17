produto=str(input("qual é o produto desejado ? "))

valor_do_produto = float(input("qual o valor do produto "))

quantidade_do_produto = int(input("quntidade do produto "))

valor_total = valor_do_produto*quantidade_do_produto

valor_total_com_desconto = valor_do_produto*quantidade_do_produto

if quantidade_do_produto >= 5:
    valor_total_com_desconto=valor_total_com_desconto*(4/5)
    print(f"{quantidade_do_produto} {produto} por {valor_do_produto} sai a {valor_total}, mas com 20% de desconta sai a {valor_total_com_desconto}")
else:
    print(f"{quantidade_do_produto} {produto} por {valor_do_produto} sai a {valor_total} pois não tem desconto")