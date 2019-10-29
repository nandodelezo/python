##Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide:
##Escribe un número: 6
##scribe un número mayor que 6: 6
##6 no es mayor que 6. Vuelve a introducir un número: 1
##1 no es mayor que 6. Vuelve a introducir un número: 8
##Los números que has escrito son 6 y 8

num1=int(input("Introduce un número "))
num2=int(input("Ahora introduce un número mayor que el anterior "))
while (num1>=num2):
    num2=int(input("Ese número no es mayor que %d así que introduce otro que cumpla la condición." %(num1)))

print ("Has introducido el" ,num1, "y" ,num2,)
