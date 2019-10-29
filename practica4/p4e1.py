num1=int(input("Escribe el primer número"))
num2=int(input("Escribe el segundo número"))
num3=int(input("Escribe el tercer número"))
num4=int(input("Escribe el cuarto número"))
num5=int(input("Escribe el quinto número"))
if (num1>num2) and (num1>num3) and (num1>num4) and (num1>num5):
    print ("El número más grande es" ,num1,)
elif (num2>num1) and (num2>num3) and (num2>num4) and (num1>num5):
    print ("El número más grande es" ,num2,)
elif (num3>num1) and (num3>num2) and (num3>num4) and (num3>num5):
    print ("El número más grande es" ,num3,)
elif (num4>num1) and (num4>num2) and (num4>num3) and (num4>num5):
    print ("El número más grande es" ,num4,)
elif (num5>num1) and (num5>num2) and (num5>num3) and (num5>num4):
    print ("El número más grande es" ,num5,)
else:
    print ("Algo raro ha pasado")

if (num1<num2) and (num1<num3) and (num1<num4) and (num1<num5):
    print ("El número más pequeño es" ,num1,)
elif (num2<num1) and (num2<num3) and (num2<num4) and (num1<num5):
    print ("El número más pequeño es" ,num2,)
elif (num3<num1) and (num3<num2) and (num3<num4) and (num3<num5):
    print ("El número más pequeño es" ,num3,)
elif (num4<num1) and (num4<num2) and (num4<num3) and (num4<num5):
    print ("El número más pequeño es" ,num4,)
elif (num5<num1) and (num5<num2) and (num5<num3) and (num5<num4):
    print ("El número más pequeño es" ,num5,)
else:
    print ("Algo raro ha pasado")
