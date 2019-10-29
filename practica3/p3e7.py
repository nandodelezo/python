dia=int(input ("Introduce el día "))
mes=int(input ("Introduce el mes "))
año=int(input ("Introduce el año "))
if (dia>31) or (dia<1):
    print ("La fecha introducida no es correcta")
elif (mes==2) and (dia>28):
    print ("La fecha introducida no es correcta")
elif (mes==4) and (dia>30):
    print ("La fecha introducida no es correcta")
elif (mes==6) and (dia>30):
    print ("La fecha introducida no es correcta")
elif (mes==9) and (dia>30):
    print ("La fecha introducida no es correcta")
elif (mes==11) and (dia>30):
    print ("La fecha introducida no es correcta")
elif (mes>12) or (mes<1):
    print ("La fecha introducida no es correcta")
else:
    print ("La fecha introducida es" ,dia,"-",mes,"-",año, "y es correcta.")
