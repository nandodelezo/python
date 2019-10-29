num1=int(input("Escribe el primer número"))
num2=int(input("Escribe el segundo número"))
num3=int(input("Escribe el tercer número"))
num4=int(input("Escribe el cuarto número"))
num5=int(input("Escribe el quinto número"))
if (num1>num2) and (num1>num3) and (num1>num4) and (num1>num5):
    print ("Has colocado los números en orden decreciente")
elif (num1<num2) and (num1<num3) and (num1<num4) and (num1<num5):
    print ("Has colocado los números en orden creciente")
else:
    print ("Has colocado los números desordenados")
