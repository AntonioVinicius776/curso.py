osnum=[]
pares=[]
impares=[]
a=0
b=0
c=0

nd=int(input("numero desejado "))

for i in range(nd):
    n=int(input("da num "))
    osnum.append(n)
    if n %2 == 0 :
        pares.append(n)
        a=a+1
    else:
        impares.append(n)
        b=b+1

print(f"todos {nd} os numeros ", osnum)
print(f"todos {a} os numeros pares ", pares)
print(f"todos {b} os numeros impares ", impares)