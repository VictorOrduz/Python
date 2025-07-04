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
    if not isbn:
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
    global socios, auxContador

    print("================================================================")
    print("Registrar Socio 👤")
    print("================================================================")
    print("Digite 0 si quiere cancelar la creacion")

    nombre = input("Nombre del socio: ").strip().lower()
    
    if nombre == "0": return

    if not nombre:
        print("❌ El nombre no puede estar vacío ❌")
        return

    apellido = input("Apellido del socio: ").strip().lower()

    if apellido == "0": return

    if not apellido:
        print("❌ El apellido no puede estar vacío ❌")
        return

    email = input("Email del socio: ").strip().lower()

    if email == "0": return

    if not email:
        print("❌ El email no puede estar vacío ❌")
        return
    
    # Verificar si ya existe un socio con ese email
    for socio in socios:
        if socio['email'] == email:
            print(f"❌ Ya existe un socio con el email {email} ❌")
            return

    # Crear el nuevo socio
    nuevo_socio = {
        'id': f'Socio-{auxContador:03d}',
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'libros_prestados': []
    }

    socios.append(nuevo_socio)
    auxContador += 1
    
    print("✅ Socio Registrado Exitosamente 👤")
    print(f"👤 {nombre} {apellido}")
    print(f"📧 Email: {email}")
    print(f"🆔 ID: {nuevo_socio['id']}")
    print("================================================================")

def prestrarLibro():
    global libros, socios
    
    print("PRESTAMO DE LIBROS")
    
    isbn = ("digite el isbn del libro a prestar: ").strip()
    
    if not isbn:
        print("❌ el ISBN no puede estar vacio ❌")   
        return
    
    libroEncontrado = None
    
    for libro in libros:
        if libro['isbn'] == isbn:
            libroEncontrado = libro
            break
            
    if not libroEncontrado:
        print(f"❌ no existe un libro con ISBN {isbn} ❌")
        return
    
    id_socio = input("ID del socio: ").strip()
    print(id_socio)
    
    if not id_socio:
        print("el ID no puede estar vacio")
        return

    idSocioEncontrado = None
    for socio in socios:
        if socio['id'] == id_socio:
            idSocioEncontrado = socio
            break
        
    if not idSocioEncontrado:
        print(f"NO se encontro un usuario con el ID {id_socio}")
        return
    
    disponibleLibro = None
    for libro in libros:
        if libro['estado'] == 'Disponible':
            disponibleLibro = True
            break
        
    if not disponibleLibro:
        print("Actualmente el libro solicitado no esta disponible")
        return
    
    libroEncontrado['estado'] == 'Prestado'
    libroEncontrado['socio_prestado'] = id_socio
    
    print("libro pretado con exito")
    print({libroEncontrado['titulo']})
    print(f"libro prestado a {idSocioEncontrado['nombre']}")
               
def devolverLibro():
    global libros
    
    isbn = input("ISBN del libro a prestar: ").strip()
    
    if not isbn:
        print(" el ISBN no puede estar vacio")
        return

    libroEncontrado = None
    for libro in libros:
        if libro['isbn'] == isbn:
            libroEncontrado = libro
            break
        
    if not libroEncontrado:
        print(f"no se encontro un libro con el ISBN {isbn}")
        return
    
    libroEncontrado['estado'] = 'Disponible'
    libroEncontrado['socio_prestado'] = None
    
    print("Libro devuelto exitosamente")

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
    table = PrettyTable()

    table.field_names = ["ID", "Nombre", "Apellido", "Email", "Libros Prestados"]

    table.title = "👤 Mostrando Socios 👤"

    if not socios:
        print("================================================================")
        print("No hay socios registrados en la biblioteca")
        print("================================================================")
        return

    for socio in socios:
        libros_prestados = len(socio["libros_prestados"])
        table.add_row([socio["id"], socio["nombre"], socio["apellido"], socio["email"], libros_prestados])

    print(table)

    """
    print("================================================================")
    print("Mostrando todos los socios")
    print("================================================================")

    if not socios:
        print("No hay socios registrados en la biblioteca")
        return
    
    for i, socio in enumerate(socios, 1):
        print("================================================================")
        print(f"{i}. ID: {socio["id"]}")
        print(f"     Nombre: {socio["nombre"]} {socio["apellido"]}")
        print(f"     Email: {socio["email"]}")
        print(f"     Libros Prestados: {len(socio["libros_prestados"])}")
        print("================================================================")
    """
    
#funcion principal del programa
def main():
    table = PrettyTable()
    while True:
        mostrarMenu()
        opcion = input("seleccione una opcion (0-7): ").strip()
        
        match opcion:
            case '1':
                registrarLibro()
            case '2':
                registrarsocio()
            case '3':
                prestrarLibro()
            case '4':
                devolverLibro()
            case '5':
                pass
            case '6':
                verTodosLibros()
            case '7':
                verTodosSocios()
            case '0':
                print("=============================================================")
                print("😉 Gracias por usar MINIBIBLIO 😜")
                print("👍 Hasta luego ✌")
                print("=============================================================")
                break
            case _:
                print("opcion no valida, por favor seleccione una opcion del 0 al 7")

main()

