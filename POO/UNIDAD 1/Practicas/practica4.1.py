class Ticket:
    TIPOS_PERMITIDOS = ["software", "prueba"]
    PRIORIDADES_PERMITIDAS = ["alta", "media", "baja"]
    
    def __init__(self, id, tipo, prioridad):
        if tipo not in self.TIPOS_PERMITIDOS:
            raise ValueError(f"Tipo debe ser uno de: {self.TIPOS_PERMITIDOS}")
        if prioridad not in self.PRIORIDADES_PERMITIDAS:
            raise ValueError(f"Prioridad debe ser una de: {self.PRIORIDADES_PERMITIDAS}")
        
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "pendiente"
        self.empleado_asignado = None

    def mostrar_informacion(self):
        empleado = self.empleado_asignado.nombre if self.empleado_asignado else "Sin asignar"
        return f"Ticket {self.id}: Tipo: {self.tipo}, Prioridad: {self.prioridad}, Estado: {self.estado}, Empleado: {empleado}"

class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
    
    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} está trabajando en el ticket {ticket.id}.")

class Desarrollador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Desarrollador")
    
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"El desarrollador {self.nombre} ha resuelto el ticket {ticket.id}.")
        else:
            print(f"El desarrollador {self.nombre} no puede trabajar en tickets de tipo {ticket.tipo}")

class Tester(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Tester")
    
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"El tester {self.nombre} ha probado el ticket {ticket.id}.")
        else:
            print(f"El tester {self.nombre} no puede trabajar en tickets de tipo {ticket.tipo}")

class ProjectManager(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Project Manager")
    
    def asignar_ticket(self, ticket, empleado):
        ticket.empleado_asignado = empleado
        print(f"{self.nombre} ha asignado el ticket {ticket.id} al empleado {empleado.nombre}.")
        empleado.trabajar_en_ticket(ticket)

# Listas globales para almacenar tickets y empleados
tickets = []
empleados = []

# Crear algunos empleados por defecto
empleados.append(Desarrollador("Carlitos"))
empleados.append(Tester("Juanillo"))
empleados.append(ProjectManager("Marianita"))
empleados.append(Desarrollador("Ana"))
empleados.append(Tester("Pedro"))

# Función para crear tickets
def crear_ticket():
    print("\n--- CREAR NUEVO TICKET ---")
    try:
        id = len(tickets) + 1
        print("Tipos disponibles: software, prueba")
        tipo = input("Ingrese el tipo de ticket: ").lower()
        print("Prioridades disponibles: alta, media, baja")
        prioridad = input("Ingrese la prioridad: ").lower()
        
        ticket = Ticket(id, tipo, prioridad)
        tickets.append(ticket)
        print(f"✅ Ticket {id} creado exitosamente!")
        
    except ValueError as e:
        print(f"❌ Error: {e}")

# Función para ver tickets
def ver_tickets():
    print("\n--- LISTA DE TICKETS ---")
    if not tickets:
        print("No hay tickets creados.")
    else:
        for ticket in tickets:
            print(ticket.mostrar_informacion())

# Función para asignar tickets
def asignar_ticket():
    print("\n--- ASIGNAR TICKET ---")
    
    if not tickets:
        print("No hay tickets disponibles para asignar.")
        return
    
    if not empleados:
        print("No hay empleados disponibles.")
        return
    
    # Mostrar tickets disponibles
    print("Tickets disponibles:")
    for ticket in tickets:
        if ticket.estado == "pendiente":
            print(ticket.mostrar_informacion())
    
    try:
        ticket_id = int(input("Ingrese el ID del ticket a asignar: "))
        ticket_seleccionado = None
        
        for ticket in tickets:
            if ticket.id == ticket_id and ticket.estado == "pendiente":
                ticket_seleccionado = ticket
                break
        
        if not ticket_seleccionado:
            print("❌ Ticket no encontrado o ya está resuelto.")
            return
        
        # Mostrar empleados disponibles
        print("\nEmpleados disponibles:")
        for i, empleado in enumerate(empleados, 1):
            print(f"{i}. {empleado.nombre} ({empleado.rol})")
        
        empleado_idx = int(input("Seleccione el número del empleado: ")) - 1
        
        if 0 <= empleado_idx < len(empleados):
            empleado_seleccionado = empleados[empleado_idx]
            
            # Buscar un Project Manager para hacer la asignación
            pm = None
            for empleado in empleados:
                if empleado.rol == "Project Manager":
                    pm = empleado
                    break
            
            if pm:
                pm.asignar_ticket(ticket_seleccionado, empleado_seleccionado)
            else:
                # Si no hay PM, asignar directamente
                ticket_seleccionado.empleado_asignado = empleado_seleccionado
                empleado_seleccionado.trabajar_en_ticket(ticket_seleccionado)
                
            print("✅ Ticket asignado exitosamente!")
        else:
            print("❌ Selección de empleado inválida.")
            
    except ValueError:
        print("❌ Por favor, ingrese un número válido.")

# Función para guardar tickets en archivo
def guardar_tickets():
    print("\n--- GUARDAR TICKETS ---")
    if not tickets:
        print("No hay tickets para guardar.")
        return
    
    try:
        with open("tickets.txt", "w", encoding="utf-8") as archivo:
            archivo.write("=== LISTA DE TICKETS ===\n")
            for ticket in tickets:
                empleado = ticket.empleado_asignado.nombre if ticket.empleado_asignado else "Sin asignar"
                archivo.write(f"Ticket {ticket.id}: Tipo: {ticket.tipo}, Prioridad: {ticket.prioridad}, Estado: {ticket.estado}, Empleado: {empleado}\n")
        
        print("✅ Tickets guardados en 'tickets.txt'")
    except Exception as e:
        print(f"❌ Error al guardar los tickets: {e}")

# Función para ver empleados
def ver_empleados():
    print("\n--- LISTA DE EMPLEADOS ---")
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for i, empleado in enumerate(empleados, 1):
            print(f"{i}. {empleado.nombre} - {empleado.rol}")

# Función para mostrar el menú
def mostrar_menu():
    print("\n" + "="*50)
    print("          SISTEMA DE GESTIÓN DE TICKETS")
    print("="*50)
    print("1. Crear tickets")
    print("2. Ver los tickets")
    print("3. Asignar un ticket")
    print("4. Guardar tickets en archivo txt")
    print("5. Ver empleados")
    print("6. Salir")
    print("="*50)

# Programa principal
def main():
    print("Bienvenido al Sistema de Gestión de Tickets")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-6): ")
            
            if opcion == "1":
                crear_ticket()
            elif opcion == "2":
                ver_tickets()
            elif opcion == "3":
                asignar_ticket()
            elif opcion == "4":
                guardar_tickets()
            elif opcion == "5":
                ver_empleados()
            elif opcion == "6":
                print("¡Gracias por usar el sistema! ¡Hasta pronto!")
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-6.")
        
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()