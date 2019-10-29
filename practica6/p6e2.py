listado=[]
listing=True
while (listing==True):
    print ("Introduce un número para almacenarlo en una lista\n")
    var1=input("")
    listado.append(var1)
    print("Has introducido" ,listado,)
    salir=input("Ahora escribe Salir para salir o pulsa ENTER para continuar.\n")
    if (salir=="Salir") or (salir=="salir"):
        print("Finalmente la lista contiene los siguientes números:" ,listado,)
        listing=False
