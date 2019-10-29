listado=[]
listing=True
while (listing==True):
    print ("Introduce una palabra para almacenarlas en la lista\n")
    var1=input("")
    listado.append(var1)
    print("Has introducido" ,listado,)
    salir=input("Ahora pulsa S para salir o cualquier otra letra para añadir otra palabra\n")
    if (salir=="S") or (salir=="s"):
        print("Finalmente la lista contiene" ,listado,)
        listing=False
