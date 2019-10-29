numlim = int(input("Introduce un número que será el límite"))
listanumeros = []
sumatotal = 0

while (sumatotal < numlim):
    masnum = int(input("Aún no se ha excedido el valor límite, puedes  introducir otro número"))
    listanumeros.append(masnum)
    sumatotal = sumatotal + masnum

print("Los números han excedido el límite: ")
for i in listanumeros:
    if (listanumeros[-1]):
        print (i, end=", ")
    else:
        print (i, end=". ")
