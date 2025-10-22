class Libro:  # Los nombres de clases deben usar CamelCase
    def __init__(self, titulo, autor, anio, codigo):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.codigo = codigo
        self.disponible = True
        
    def mostrar_info(self):
        estado = "disponible" if self.disponible else "no disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}, Código: {self.codigo}, Estado: {estado}")
        
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
            return True
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")
            return False
            
    def disponibilidad(self):  # Este método debería llamarse 'devolver'
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto y está disponible.")
        
class Usuario:  # CamelCase
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, ID: {self.id_usuario}, Correo: {self.correo}")
        
    def sol_prestamo(self, libro):
        if libro.disponible:
            print(f"{self.nombre} ha solicitado el préstamo del libro '{libro.titulo}'.")
            return True
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")
            return False
        
class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario, correo, grado, grupo):
        super().__init__(nombre, id_usuario, correo)
        self.grado = grado
        self.grupo = grupo
        # ERROR: Se eliminaron 'carrera' y 'semestre' que no estaban en los parámetros
        
    def mostrar_info(self):
        print(f"--- Información del Usuario (Estudiante) ---")
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id_usuario}")
        print(f"Correo: {self.correo}")
        print(f"Grado: {self.grado}")  # Corregido: usar grado en lugar de carrera
        print(f"Grupo: {self.grupo}")  # Corregido: usar grupo en lugar de semestre
        
class Profesor(Usuario):
    def __init__(self, nombre, id_usuario, correo, departamento, tipo_contrato):
        super().__init__(nombre, id_usuario, correo)
        self.departamento = departamento
        self.tipo_contrato = tipo_contrato
        
    def mostrar_info(self):
        print(f"--- Información del Usuario (Profesor) ---")
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id_usuario}")
        print(f"Correo: {self.correo}")
        print(f"Departamento: {self.departamento}")
        print(f"Contrato: {self.tipo_contrato}")
        
class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        
    def registrar_prestamo(self):
        print(f"--- Información del Préstamo ---")
        print(f"Libro: {self.libro.titulo}")
        print(f"Usuario: {self.usuario.nombre}")
        print(f"Fecha de Préstamo: {self.fecha_prestamo}")
        print(f"Fecha de Devolución: {self.fecha_devolucion}")
        
    def devolver_libro(self):
        if not self.libro.disponible:
            self.libro.disponibilidad()
            print(f"El libro '{self.libro.titulo}' ha sido devuelto por {self.usuario.nombre}.")
            return True
        else:
            print(f"El libro '{self.libro.titulo}' no estaba prestado.")
            return False
        
# PROGRAMA PRINCIPAL CORREGIDO
print("----- Sistema de Gestión de Biblioteca -----")

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "LB001")
libro2 = Libro("1984", "George Orwell", 1949, "LB002")

estudiante1 = Estudiante("Jesus Mendoza", "ST123", "jesus.M@utd.edu.com", "Software", 4)
profesor1 = Profesor("Pedro Said Vara Chacón", "PR456", "pedro.V@edu.com", "POO", "Tiempo Completo")

print("\n--- Información de Usuarios ---")
usuario_base = Usuario("Juan Nadie", "GEN001", "juan.n@general.com")
usuario_base.mostrar_info()
print("-" * 30)

estudiante1.mostrar_info()
print("-" * 30)

profesor1.mostrar_info()
print("-" * 30)

print("\n--- Estado inicial del libro ---")
libro1.mostrar_info()
print("\n" + "="*50 + "\n")

print("--- Préstamo por estudiante ---")
# Primero verificar si puede solicitar el préstamo
if estudiante1.sol_prestamo(libro1):
    # Si puede solicitar, crear el préstamo y prestar el libro
    if libro1.prestar():  # El método prestar ahora devuelve True/False
        prestamo_estudiante = Prestamo(libro1, estudiante1, "2025-10-07", "2025-10-21")
        prestamo_estudiante.registrar_prestamo()
    
print("\n--- Estado del libro después del préstamo ---")
libro1.mostrar_info()
print("\n" + "="*50 + "\n")

print("--- Intento de préstamo no disponible ---")
profesor1.sol_prestamo(libro1)
print("\n" + "="*50 + "\n")

print("--- Devolución del libro por el estudiante ---")
if 'prestamo_estudiante' in locals():  # Verificar que el préstamo existe
    prestamo_estudiante.devolver_libro()
print("\n")  # Corregido: era "/n" en lugar de "\n"
    
print("------ Estado final del libro ------")
libro1.mostrar_info()
print("\n" + "="*50 + "\n")