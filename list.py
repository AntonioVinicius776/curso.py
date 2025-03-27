list0=["a", "c", "b", "d"]
print(list0)

list0[0]="nossa"
print(list0[0])
print(list0)

del list0[3]
print(list0)

list0.append("e")
print(list0)

list0.sort()
print(list0)

list0.sort(reverse=True)
print(list0)

print(max(list0))

print(min(list0))

print(list0)

print(list0.index("nossa"))

print(list0[3])

print(list0.count("nossa"))

list1=["receba"]

list2=list0+list1

print(list2)

#antonio vinicius marinho souza