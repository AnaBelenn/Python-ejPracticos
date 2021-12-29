tupla=("Plastico","Petroleo","Deshechos de fabricas")
op = 1
while op!=0:
    op = int(input("Elija un numero :  "))
    if op>len(tupla):
        print("Error fuera del límite")
        continue

    elif op==0:
        continue

    else:
        print(tupla[op-1])
else:
    print("Finalizando programa...")