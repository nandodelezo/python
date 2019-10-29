num1=int(input("Escribe un primer número\n"))
print ("De momento tienes el" ,num1,)
num2=int(input("Ahora escribe un segundo número\n"))
print ("De momento tienes el" ,num1, "y el" ,num2,)
num3=int(input("Escribe el tercer y último número\n"))
print ("Tienes el" ,num1, "el" ,num2, "y el" ,num3,)
num4=int(input("Ahora escribe el número para comprobar si es divisor de esos 3\n"))
if (num1%num4==0) and (num2%num4==0) and (num3%num4==0):
    print ("Efectivamente, el" ,num4, "es divisor de los 3 anteriores")
else:
    print ("El número que has introducido NO es divisor de los 3 anteriores")
