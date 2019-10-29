num1=int(input("Escribe un número\n"))
num2=int(input("Escribe otro número que sea mayor\n"))
for i in range(num1,num2+1):
    if (i%2==0):
        print ("El número" ,i, "es par")
    else:
        print ("El número" ,i, "es impar")
