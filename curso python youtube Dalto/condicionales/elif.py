ingreso_mensual = 100000
gasto_mensual = 600000

#ejemplo de if anidado y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 50000: 
        print("te alcanza")
    else:
        print("no te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venzuela")
    
else:
    print ("sos pobre")