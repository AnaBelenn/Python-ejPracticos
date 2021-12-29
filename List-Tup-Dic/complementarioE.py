'''
Cargar m elementos en una pila, y luego copiarlos en una nueva lista.
'''
m=int(input("Cuantos elementos desea cargar? \n"))
lista=[]
nueva_lista=[]
for elto in range(m):
    lista.append(input("Ingrese el elemento:\n"))

nueva_lista=lista.copy()
print(f"Lista original: {lista}")
print(f"Nueva lista: {nueva_lista}")