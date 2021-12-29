'''
Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.
'''
lista1=[1, 2, 3, 4, 5]
lista2=["A", "B", "C", "D", "E"]
for n in lista2:
    if n in lista1:
        continue
    else:
        lista1.append(n)
print(lista1)