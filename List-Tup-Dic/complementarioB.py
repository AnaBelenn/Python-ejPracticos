'''
Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada componente sea igual al cuadrado del 
componente original. El programa mostrara la lista resultante por pantalla.
'''
lista=list()
for n in range(5):
    lista.append(int(input("Ingrese un numero: \n")))
print(f"Lista original: \n{lista}")
for elto in range(len(lista)):
    lista[elto]=(lista[elto])**2
print(f"Lista resultante: \n{lista}")