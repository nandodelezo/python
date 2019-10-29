area=input("Escribe \"cuadrado\" o \"triángulo\" según el área de lo que quieras calcular\n")
if (area=="triangulo") or (area=="triángulo"):
    basetri=int(input("Escribe la base\n"))
    altutri=int(input("Escribe la altura\n"))
    resultado=(basetri*altutri)/2
    print ("El área del triángulo es" ,resultado,)
else:
    lado=int(input("Escribe el lado del cuadrado\n"))
    resultado=(lado*lado)
    print ("El área del cuadrado es" ,resultado,)

