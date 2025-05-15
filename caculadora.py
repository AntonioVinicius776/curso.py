print("insira os dois numeros")
n0=int(input())
n1=int(input())

esc0=int(input("o que deseja ?\n1-somar\n2-subtrair\n3-multiplicar\n4-dividir\n5-sair\n"))
while esc0 !=5 :
    
    if esc0==1:
        print("soma", n0+n1)
    elif esc0==2:
        print("sub", n0-n1)
    elif esc0==3:
        print("multi", n0*n1)
    elif esc0==4:
        print("div", n0/n1)
        
    esc0=int(input("o que deseja ?\n1-somar\n2-subtrair\n3-multiplicar\n4-dividir\n5-sair\n"))

else:
    print("tenha um bom dia")
