##Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios.
##Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales.
##El programa termina escribiendo la lista de números.
##Escribe un número: 6
##Escribe un número mayor que 6: 4
##4 no es mayor que 6. Vuelve a probar: 50
##Escribe un número entre 6 y 50: 45
##Escribe otro número entre 6 y 50: 13
##Escribe otro número entre 6 y 50: 4
##Los números situados entre 6 y 50 que has escrito son: 45, 13 

num1=int(input("Introduce un número "))
num2=int(input("Ahora introduce un número mayor que el anterior "))
while (num1>=num2):
    num2=int(input("Ese número no es mayor que %d así que introduce otro que cumpla la condición.\n" %(num1)))

print ("De momento has introducido" ,num1, "y" ,num2,)
num3=int(input("Ahora introduce un número que esté entre los que has introducido "))
while (num3<=num1) or (num3>=num2):
    num3=int(input("Ese número no es mayor que %d y %d así que introduce otro que cumpla la condición.\n" %(num1,num2)))

print ("Ahora vas a introducir otro, recordemos tu rango:" ,num1, "y" ,num2,)
num4=int(input("Ahora introduce un número que esté entre los que has introducido "))
while (num4<=num1) or (num4>=num2):
    num4=int(input("Ese número no es mayor que %d y %d así que introduce otro que cumpla la condición.\n" %(num1,num2)))


print ("Los números situados entre" ,num1, "y" ,num2, "que has escrito son" ,num3, "y" ,num4,)
