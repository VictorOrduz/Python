cursosdevsenior = ["python","java","javascript","IA"]

def mostrar_menu():
    print("\n DEV SENIOR STARTUP")
    print("1. ver cursos disponibles")
    print("2. agregar un nuevo curso")
    print("3. eliminar un curso")
    print("4. buscar un curso")
    print("5. salir")
    
def ver_cursos():
    print("\n CURSOS DISPONIBLES")
    for idx, curso in enumerate(cursosdevsenior, 1):
        print(f"{idx}. {curso}")

def agregar_curso():
    nuevocurso = input("ingrese el nuevo curso a DevSenior: ").strip()
    if nuevocurso:
        cursosdevsenior.append(nuevocurso)
        print(f"curso {nuevocurso} agregado exitosamente")
        
def eliminar_curso():
    ver_cursos()
    try:
        indice = int(input("ingrese el numero del curso que desee eliminar: "))
        if indice > 0 and indice <= len(cursosdevsenior):
            cursoeliminado = cursosdevsenior.pop(indice -1)
            print(f"CURSO {cursoeliminado} ELIMINADO SATISFACTORIAMENTE")
        else:
            print("numero invalido")
                     
    except ValueError:
        print("debes ingresar valores numericos")

def buscar_curso():
    nombrebuscar = input("ingrese el nombre del curso que desea buscar: ").strip().lower()
    encontrados = [curso for curso in cursosdevsenior if nombrebuscar in curso.lower()]
    if encontrados:
        print("\n CURSOS ENCONTRADOS")
        for curso in encontrados:
            print(curso)
    else:
        print("no se encontro curso con ese nombre")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("ingrese una opcion: "))
        
        if opcion == 1:
            ver_cursos()
        elif opcion == 2:
            agregar_curso()
        elif opcion == 3:
            eliminar_curso()
        elif opcion == 4:
            buscar_curso()
        elif opcion == 5:
            print("saliendo de la aplicacion...")
            break
        else:
            print("opcion invalida")

if __name__ == "__main__":
    main()
                                    