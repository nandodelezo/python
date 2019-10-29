listado=[]
num1=int(input("Introduce un número: "))
listado.append(num1)
num2=int(input("Ahora otro mayor que %d: " %(num1)))
while(num2>num1):
    listado.append(num2)
    num1=num2
    num2=int(input("Introduce otro aún mayor "))

ltt=listado
print ("Los numeros son:" ,ltt,)
