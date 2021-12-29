def separar(lista):
    listaMas100={}
    listaMenos100={}

    for x,val in lista.items():
        if val>=100:
            listaMas100[x]=val
        elif val<100:
            listaMenos100[x]=val


    return listaMas100, listaMenos100

cantidad_arboles = {"Resistencia":120, "Saenz Peña":33,"Charata":134,"Quitilipi":300,"V.Angela":100,"Barranqueras":140,"Napenay":21,"Plaza":400}

lista1,lista2= separar(cantidad_arboles)

print(f"Ciudades que plantaron mas de 100 arboles es {lista1} - Cantidad : {len(lista1)}")
print(f"Ciudades que plantaron menos de 100 arboles es {lista2} - Cantidad : {len(lista2)}")