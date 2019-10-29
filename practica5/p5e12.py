num1=int(input("Escribe un número para saber si es primo o no"))
for i in range (2, num1-1):
    if num1%i==0:
        print ("El número NO es primo")
    else:
        print ("El número es primo")
