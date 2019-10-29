num1=int(input("Escribe un número\n"))
num2=int(input("Escribe otro número mayor\n"))
suma=num1
for i in range(num1+1,num2+1):
    suma=suma+i
print ("El resultado de sumar todos los números entre" ,num1, "y" ,num2, "(incluyéndolos) es" ,suma,)
