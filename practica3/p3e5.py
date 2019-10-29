print ("Introduce un número que no tenga más de 3 cifras")
numero=int(input())
if (numero>999) or (numero<-999):
    print ("El número" ,numero, "no es válido pues supera las 3 cifras")
else:
    print ("El número" ,numero, "está OK.")
    
