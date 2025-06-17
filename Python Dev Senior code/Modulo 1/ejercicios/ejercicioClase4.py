'''
ENUNCIADO FINAL – SISTEMA DE VENTAS DE PROGRAMAS EDUCATIVOS EN DEV SENIOR
(SIN COLECCIONES)
La reconocida startup educativa Dev Senior Code, que forma desarrolladores de software
con validez internacional, necesita un sistema básico para registrar las ventas de sus 3
programas más demandados:
• Java de Cero a Senior
• Python con IA Aplicada
• Mobile Senior con IA
Cada programa tiene un valor oficial de $18.000.000, pero gracias a las Becas Manos al
Futuro, el estudiante accede con un 90% de descuento, pagando únicamente $1.800.000
por todo el programa.
El sistema debe permitir a los asesores académicos:
1. Mostrar los programas disponibles, con su precio con descuento.
2. Registrar la venta de cualquiera de los tres programas, indicando la cantidad de
estudiantes matriculados.
3. Consultar los ingresos acumulados por cada programa.
4. Mostrar el total general de ingresos del día.
5. Salir del sistema.
Requisitos técnicos:
• Cada funcionalidad debe estar implementada en una función.
• Solo deben utilizarse variables simples (por ejemplo: programa1, precio1,
ventas1…), no se permite el uso de listas, diccionarios ni ninguna estructura de
colección.
• El sistema debe utilizar un menú principal controlado con un ciclo while, que se
repite hasta que el usuario decida salir.
• Deben usarse condicionales para validar la opción ingresada y prevenir errores.
'''

programa1 = "Java de Cero a Senior"
programa2 = "Python con IA Aplicada"
programa3 = "Mobile Senior con IA"
valor = 18000000
valorDescuento = int(valor * 0.1)
valor1 = 0
valor2 = 0
valor3 = 0
estudiantes1 = 0
estudiantes2 = 0
estudiantes3 = 0

def menuPrincipal():
    print("""
          +-------------------------+
          |          MENU           |
          |1. Programas disponibles |
          |2. Consultar pagos       |
          |3. Total de ingresos     |
          |4. Salir                 |
          +-------------------------+
          """)

def programas():
    print(f"""
          +-------------------------------------------+
          |           PROGRAMAS DISPONIBLES           |
          |1. {programa1}, valor: ${valorDescuento}  |
          |2. {programa2}, valor: ${valorDescuento} |
          |3. {programa3}, valor: ${valorDescuento}   |
          |4. salir                                   |
          +-------------------------------------------+
          """)
def venta1():
  global valor1, estudiantes1
  cantidadEstudiantes1 = int(input(f"ingrese la cantidad de estudiantes a matricularse en {programa1}: "))
  if cantidadEstudiantes1 > 0:
    cantidadValor1 = cantidadEstudiantes1 * valorDescuento
    valor1 += cantidadValor1
    estudiantes1 += cantidadEstudiantes1
    return
  else:
    print("ingrese un valor admitido")

def venta2():
  global valor2, estudiantes2
  cantidadEstudiantes2 = int(input(f"ingrese la cantidad de estudiantes a matricularse en {programa2}: "))
  if cantidadEstudiantes2 > 0:
    cantidadValor2 = cantidadEstudiantes2 * valorDescuento
    valor2 += cantidadValor2
    estudiantes2 += cantidadEstudiantes2
    return 
  else:
    print("ingrese un valor admitido")
   
def venta3(): 
  global valor3, estudiantes3        
  cantidadEstudiantes3 = int(input(f"ingrese la cantidad de estudiantes a matricularse en {programa3}: "))
  if cantidadEstudiantes3 > 0:
    cantidadValor3 = cantidadEstudiantes3 * valorDescuento
    valor3 += cantidadValor3
    estudiantes3 += cantidadEstudiantes3
    return
  else:
    print("ingrese un valor admitido")
       
def consultaPagos():
  print(f"el valor total pagado por el programa {programa1}, es de ${valor1}")
  print(f"el valor total pagado por el programa {programa2}, es de ${valor2}")
  print(f"el valor total pagado por el programa {programa3}, es de ${valor3}")
  
def estadisticaFinal():
  print(f"{estudiantes1} estudiantes se han matriculado para el programa {programa1}")
  print(f"{estudiantes2} estudiantes se han matriculado para el programa {programa2}")
  print(f"{estudiantes3} estudiantes se han matriculado para el programa {programa3}")
  print(f"el total de dinero recaudado por concepto de matricula es de ${valor1 + valor2 + valor3} ")
    
while True:
  menuPrincipal()
  opcion = int(input("ingrese una opcion del menu: "))  
  if opcion == 1:
    while True:
      programas()
      opcion2 = int(input("seleccione el programa al cual va a matricular estudiantes: "))
      if opcion2 == 1:
        venta1()
      elif opcion2 == 2:
        venta2()
      elif opcion2 == 3:
        venta3()
      elif opcion2 == 4:
        break
      else:
        print("opcion invalida")
  elif opcion == 2:
    consultaPagos()
  elif opcion == 3:
    estadisticaFinal()
  elif opcion == 4:
    break
  else:
    print(f"por favor ingrese una opcion valida")
    