ancho=int(input("Escribe la anchura del rectángulo\n"))
alto=int(input("Escribe la altura del rectángulo\n"))

alto=alto-2
print ('*'*ancho)
for i in range(alto):
    print ('*' + ' ' * (ancho-2) + '*')
print ('*'*ancho)
