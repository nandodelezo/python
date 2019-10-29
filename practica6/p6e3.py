print ("Introduce notas con valor comprendido entre 0 y 10. Introduce una nota fuera de dichos valores para dejar de introducir notas.")
listado=[]
nota=0

while ((nota>=0) and (nota<=10)):
    nota=float(input("Introduce una nota "))
    if ((nota>=0) and (nota<=10)):
        listado.append(nota)
print ("Has introducido las siguientes notas" ,listado,)
