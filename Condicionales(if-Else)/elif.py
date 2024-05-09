ingreso_mensual = 100
gasto_mensual = 10000

#if anidado y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien economicamente")
    else:
        print("Estas gastando mucho, capaz no te alcanza")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")

elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
else:
    print("Sos pobre")