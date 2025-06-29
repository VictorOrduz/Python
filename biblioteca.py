from prettytable import PrettyTable

#base de datos en memoria
libros = [
    {
        'isbn': '1',
        'titulo': 'La Odisea',
        'autor': 'Homero',
        'estado': 'disponible',
        'socio_prestado': None
    },
    {
        'isbn': '2',
        'titulo': 'Don Quijote de la Mancha',
        'autor': 'Miguel de Cervantes',
        'estado': 'disponible',
        'socio_prestado': None
    },
    {
        'isbn': '3',
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'estado': 'disponible',
        'socio_prestado': None
    },
    {
        'isbn': '4',
        'titulo': '1984',
        'autor': 'George Orwell',
        'estado': 'disponible',
        'socio_prestado': None
    },
    {
        'isbn': '5',
        'titulo': 'La casa de Bernarda Alba',
        'autor': 'Federico García Lorca',
        'estado': 'disponible',
        'socio_prestado': None
    }
]
socios = []

auxContador = 1

#muestra las opciones del menu
def mostrarMenu():
    print()
    print("MINIBIBLIOTECA")
    print("1. registrar libro")
    print("2. registrar un socio")
    print("3. prestar libro")
    print("4. devolver libro")
    print("5. ver libros prestados")
    print("6. ver todos los libros")
    print("7. ver todos los socios")
    print("0. salir")

def registrarLibro():
    global libros
    print("=============================================================")
    print("registrar libros 📚📚")
    print("=============================================================")
    print("digite cero (0), si quiere cancelar la creacion del libro")
    
    titulo = input("Titulo del libro: ").strip().lower()
    
    if titulo == '0': return     
    if not titulo:
        print("❌ el Titulo no puede estar vacio ❌")
        return  
      
    autor = input("Autor del libro: ").strip().lower()
    if autor == '0': return
    if not autor:
        print("❌ el Autor no puede estar vacio ❌")
        return
    
    isbn = input("ISBN del libro: ").strip().lower()
    if isbn == '0': return
    if not autor:
        print("❌ el ISBN no puede estar vacio ❌")   
        return
    
    for libro in libros:
        if libro['isbn'] == isbn:
            print(f"❌ ya existe un libro con ISBN {isbn} ❌") 

    #crear nuevo libro
    nuevo_libro = {
        'isbn' : isbn,
        'titulo': titulo,
        'autor' : autor,
        'estado' : 'disponible',
        'socio_prestado' : None,         
    }
    
    libros.append(nuevo_libro)
    print("✔ Libro registrado exitosamente ✔")
    print(f"📖 {titulo} - {autor}")
    print(f"ISBN: {isbn}")
    
    print("=============================================================")
    
def registrarsocio():
    pass
def prestrarLibro():
    pass
def devolverLibro():
    pass
def verLibrosPrestados():
    pass
def verTodosLibros():
    '''
    print("=============================================================")
    print("MOSTRANDO TODOS LOS LIBROS")
    print("=============================================================")
    
    if not libros:
        print("no hay libros registrados")
        return
    for i, libro in enumerate(libros, 1):
        print("=============================================================")
        print(f"{i}. Nombre del libro: {libro["titulo"]}")    
        print(f"   Autor: {libro["autor"]}")    
        print(f"   ISBN: {libro["isbn"]}")    
        print(f"   Estado: {libro["estado"]}")    
        print("=============================================================")
    '''
    table = PrettyTable()
    table.field_names = ["titulo", "Area", "isbn", "estado"]
    table.title = "📚 MOSTRANDO TODOS LOS LIBROS 📚"
    for i, libro in enumerate(libros, 1):
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])
    print(table)    
    
def verTodosSocios():
    pass


#funcion principal del programaautor
def main():
    table = PrettyTable()
    while True:
        mostrarMenu()
        opcion = input("seleccione una opcion (0-7): ").strip()
        
        match opcion:
            case '1':
                registrarLibro()
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                verTodosLibros()
            case '7':
                pass
            case '0':
                print("=============================================================")
                print("😉 Gracias por usar MINIBIBLIO 😜")
                print("👍 Hasta luego ✌")
                print("=============================================================")
                break
            case _:
                print("opcion no valida, por favor seleccione una opcion del 0 al 7")

main()
