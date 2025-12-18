class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.codigo} - {self.titulo} ({self.autor}) - {estado}"


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_prestados.append(libro)


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, codigo_libro, id_usuario):
        libro = self.buscar_libro(codigo_libro)
        usuario = self.buscar_usuario(id_usuario)

        if libro and usuario:
            if libro.disponible:
                libro.disponible = False
                usuario.agregar_libro(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}")
            else:
                print("El libro no está disponible")
        else:
            print("Libro o usuario no encontrado")

    def devolver_libro(self, codigo_libro, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.codigo == codigo_libro:
                    libro.disponible = True
                    usuario.libros_prestados.remove(libro)
                    print(f"Libro '{libro.titulo}' devuelto correctamente")
                    return
        print("No se pudo devolver el libro")

    def buscar_libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None


# ------------------ PROGRAMA PRINCIPAL ------------------

biblioteca = Biblioteca()

libro1 = Libro("L001", "Python Básico", "Guido van Rossum")
libro2 = Libro("L002", "Estructuras de Datos", "Niklaus Wirth")

usuario1 = Usuario("U01", "María Pianda")

biblioteca.registrar_libro(libro1)
biblioteca.registrar_libro(libro2)
biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro("L001", "U01")
biblioteca.devolver_libro("L001", "U01")







