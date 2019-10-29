#Escribe un programa que te pida primero un número y luego te pida números hasta que la suma
#de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.
#Escribe límite: 50
#Escribe un valor: 10
#Escribe otro valor: 45
#45 es demasiado grande. Escribe otro valor: 1
#Escribe otro valor: 39
#El límite a alcanzar es 50. La lista creada es: 10, 1, 39

numlim = int(input("Introduce un número que será el límite "))
listanumeros = []
sumatotal = 0

while (sumatotal < numlim):
    masnum = int(input("Aún no has igualado el límite, introduce otro número "))
    sumatotal = sumatotal + masnum
    if (sumatotal > numlim):
        print("El número no sirve por que es demasiado grande, introduce otro ")
        sumatotal = sumatotal - masnum
    listanumeros.append(masnum)
    if (sumatotal == numlim):
        print("Has igualado el número límite ")
