cantidad=int(input("Escribe una cantidad para extraer del cajero\n"))
if (cantidad%500==0):
    print("El cajero te devuelve" ,cantidad//500, "billetes de 500€")
elif (cantidad%200==0):
    print ("El cajero te devuelve" ,cantidad//200, "billetes de 200€")
elif (cantidad%100==0):
    print ("El cajero te devuelve" ,cantidad//100, "billetes de 100€")
elif (cantidad%50==0):
    print ("El cajero te devuelve" ,cantidad//50, "billetes de 50€")
elif (cantidad%20==0):
    print ("El cajero te devuelve" ,cantidad//20, "billetes de 20€")
elif (cantidad%10==0):
    print ("El cajero te devuelve" ,cantidad//10, "billetes de 10€")
elif (cantidad%5==0):
    print ("El cajero te devuelve" ,cantidad//5, "billetes de 5€")
else:
    print ("Esta cantidad no es divisible entre los billetes disponibles")
