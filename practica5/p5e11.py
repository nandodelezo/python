num1=int(input("Introduce un número para encontrar sus divisores\n"))
print ("Los divisores de" ,num1, "son:")
for i in range (1,num1):
        if num1%i==0:
            print (i)
