#Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial.
#El programa termina escribiendo la lista de números.
#Escribe límite: 50
#Escribe un valor: 10
#Escribe otro valor: 25
#Escribe otro valor: 7
#Escribe otro valor: 14
#El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56

listanumeros = []
numlim = int(input("Introduce un número que será el límite"))

print("Ahora vas a introducir números que se sumarán. Cuando la suma supere el número límite, dejarás de introducir números")

numsum1 = int(input("Introduce el primer número para iniciar la suma"))
listanumeros.append(numsum1)
numsum2 = int(input("Ahora introduce el segundo para realizar la suma"))
listanumeros.append(numsum2)

sumatotal=numsum1+numsum2
numsum3=0

while(sumatotal+numsum3<numlim):
    numsum3 = int(input("Aún no se ha superado el número límite, introduce otro número"))
    listanumeros.append(numsum3)

print ("El límite era" ,numlim, "y tu lista la han compuesto los siguientes números:" ,listanumeros,)
