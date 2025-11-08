import tkinter as tk
from tkinter import messagebox, ttk
from user_controller import ver_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario
from product_controller import ver_productos, crear_producto, actualizar_producto, eliminar_producto


class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Dashboard - {username}")
        self.root.geometry("1000x700")   
        self.root.resizable(True, True)
        
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frames para cada pestaña
        self.frame_usuarios = ttk.Frame(self.notebook)
        self.frame_productos = ttk.Frame(self.notebook)
        
        self.notebook.add(self.frame_usuarios, text="Gestión de Usuarios")
        self.notebook.add(self.frame_productos, text="Gestión de Productos")
        
        self.crear_interfaz_usuarios()
        self.crear_interfaz_productos()
        self.root.mainloop()
        
    def crear_interfaz_usuarios(self):
        # Título
        tk.Label(self.frame_usuarios, text=f"Gestión de Usuarios - {self.username}", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        # Frame para botones de usuarios
        button_frame = tk.Frame(self.frame_usuarios)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Actualizar lista", width=15, 
                 command=self.actualizar_lista_usuarios).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Agregar usuario", width=15, 
                 command=self.agregar_usuario).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Editar usuario", width=15, 
                 command=self.editar_usuario).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Eliminar usuario", width=15, 
                 command=self.eliminar_usuario).pack(side=tk.LEFT, padx=5)
        
        # Treeview para usuarios
        self.tree_usuarios = ttk.Treeview(self.frame_usuarios, columns=("ID", "Usuario", "Rol"), show="headings", height=15)
        self.tree_usuarios.heading("ID", text="ID")
        self.tree_usuarios.heading("Usuario", text="Nombre de usuario")
        self.tree_usuarios.heading("Rol", text="Rol")
        
        self.tree_usuarios.column("ID", width=50)
        self.tree_usuarios.column("Usuario", width=200)
        self.tree_usuarios.column("Rol", width=100)
        
        self.tree_usuarios.pack(fill="both", expand=True, pady=10)
        
        # Scrollbar para usuarios
        scrollbar_usuarios = ttk.Scrollbar(self.frame_usuarios, orient="vertical", command=self.tree_usuarios.yview)
        scrollbar_usuarios.pack(side="right", fill="y")
        self.tree_usuarios.configure(yscrollcommand=scrollbar_usuarios.set)
        
        # Cargar datos iniciales
        self.actualizar_lista_usuarios()
        
    def crear_interfaz_productos(self):
        # Título
        tk.Label(self.frame_productos, text="Gestión de Productos", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        # Frame para botones de productos
        button_frame = tk.Frame(self.frame_productos)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Actualizar lista", width=15, 
                 command=self.actualizar_lista_productos).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Agregar producto", width=15, 
                 command=self.agregar_producto).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Editar producto", width=15, 
                 command=self.editar_producto).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Eliminar producto", width=15, 
                 command=self.eliminar_producto).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Cerrar sesión", width=15, 
                 command=self.cerrar_sesion).pack(side=tk.LEFT, padx=5)
        
        # Treeview para productos
        self.tree_productos = ttk.Treeview(self.frame_productos, 
                                         columns=("ID", "Nombre", "Descripción", "Stock", "Precio", "Status", "Marca", "Proveedor"), 
                                         show="headings", height=15)
        
        columnas = [
            ("ID", 50),
            ("Nombre", 150),
            ("Descripción", 200),
            ("Stock", 60),
            ("Precio", 80),
            ("Status", 70),
            ("Marca", 100),
            ("Proveedor", 120)
        ]
        
        for col, width in columnas:
            self.tree_productos.heading(col, text=col)
            self.tree_productos.column(col, width=width)
        
        self.tree_productos.pack(fill="both", expand=True, pady=10)
        
        # Scrollbar para productos
        scrollbar_productos = ttk.Scrollbar(self.frame_productos, orient="vertical", command=self.tree_productos.yview)
        scrollbar_productos.pack(side="right", fill="y")
        self.tree_productos.configure(yscrollcommand=scrollbar_productos.set)
        
        # Cargar datos iniciales
        self.actualizar_lista_productos()
        
    # MÉTODOS PARA USUARIOS (se mantienen iguales)
    def actualizar_lista_usuarios(self):
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
            
        usuarios = ver_usuarios()
        if usuarios:
            for usuario in usuarios:
                self.tree_usuarios.insert("", "end", values=usuario)
        
    def agregar_usuario(self):
        self.mostrar_formulario_usuario("Agregar Usuario")
        
    def editar_usuario(self):
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un usuario para editar.")
            return
            
        usuario_data = self.tree_usuarios.item(seleccion[0], "values")
        self.mostrar_formulario_usuario("Editar Usuario", usuario_data)
        
    def eliminar_usuario(self):
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un usuario para eliminar.")
            return
            
        usuario_data = self.tree_usuarios.item(seleccion[0], "values")
        usuario_id = usuario_data[0]
        usuario_nombre = usuario_data[1]
        
        respuesta = messagebox.askyesno(
            "Confirmar eliminación", 
            f"¿Estás seguro de que deseas eliminar al usuario '{usuario_nombre}'?"
        )
        
        if respuesta:
            if eliminar_usuario(usuario_id):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.actualizar_lista_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")
    
    def mostrar_formulario_usuario(self, titulo, usuario_data=None):
        formulario = tk.Toplevel(self.root)
        formulario.title(titulo)
        formulario.geometry("400x300")
        formulario.resizable(False, False)
        formulario.transient(self.root)
        formulario.grab_set()
        
        tk.Label(formulario, text="Usuario:", font=("Arial", 10)).pack(pady=5)
        usuario_entry = tk.Entry(formulario, width=30)
        usuario_entry.pack(pady=5)
        
        tk.Label(formulario, text="Contraseña:", font=("Arial", 10)).pack(pady=5)
        password_entry = tk.Entry(formulario, width=30, show="*")
        password_entry.pack(pady=5)
        
        tk.Label(formulario, text="Rol:", font=("Arial", 10)).pack(pady=5)
        rol_entry = tk.Entry(formulario, width=30)
        rol_entry.pack(pady=5)
        
        if usuario_data:
            usuario_entry.insert(0, usuario_data[1])
            rol_entry.insert(0, usuario_data[2])
        
        def guardar_usuario():
            usuario = usuario_entry.get().strip()
            password = password_entry.get().strip()
            rol = rol_entry.get().strip()
            
            if not usuario or not rol:
                messagebox.showwarning("Datos incompletos", "Usuario y rol son obligatorios.")
                return
                
            if usuario_data:
                if not password:
                    messagebox.showwarning("Contraseña requerida", "Para editar se requiere contraseña.")
                    return
                    
                if actualizar_usuario(usuario_data[0], usuario, password, rol):
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el usuario.")
            else:
                if not password:
                    messagebox.showwarning("Contraseña requerida", "La contraseña es obligatoria para nuevo usuario.")
                    return
                    
                if crear_usuario(usuario, password, rol):
                    messagebox.showinfo("Éxito", "Usuario creado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo crear el usuario.")
        
        tk.Button(formulario, text="Guardar", width=15, command=guardar_usuario).pack(pady=20)
        tk.Button(formulario, text="Cancelar", width=15, command=formulario.destroy).pack(pady=5)
    
    # MÉTODOS PARA PRODUCTOS
    def actualizar_lista_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
            
        productos = ver_productos()
        if productos:
            for producto in productos:
                self.tree_productos.insert("", "end", values=producto)
        
    def agregar_producto(self):
        self.mostrar_formulario_producto("Agregar Producto")
        
    def editar_producto(self):
        seleccion = self.tree_productos.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un producto para editar.")
            return
            
        producto_data = self.tree_productos.item(seleccion[0], "values")
        self.mostrar_formulario_producto("Editar Producto", producto_data)
        
    def eliminar_producto(self):
        seleccion = self.tree_productos.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un producto para eliminar.")
            return
            
        producto_data = self.tree_productos.item(seleccion[0], "values")
        producto_id = producto_data[0]
        producto_nombre = producto_data[1]
        
        respuesta = messagebox.askyesno(
            "Confirmar eliminación", 
            f"¿Estás seguro de que deseas eliminar el producto '{producto_nombre}'?"
        )
        
        if respuesta:
            if eliminar_producto(producto_id):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.actualizar_lista_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")
    
    def mostrar_formulario_producto(self, titulo, producto_data=None):
        formulario = tk.Toplevel(self.root)
        formulario.title(titulo)
        formulario.geometry("500x500")
        formulario.resizable(False, False)
        formulario.transient(self.root)
        formulario.grab_set()
        
        # Campos del formulario de producto
        campos = [
            ("Nombre Producto:", "nombre"),
            ("Descripción:", "descripcion"),
            ("Stock:", "stock"),
            ("Precio:", "precio"),
            ("Status (1=Activo, 0=Inactivo):", "status"),
            ("Marca:", "marca"),
            ("Proveedor:", "proveedor")
        ]
        
        entries = {}
        
        for label_text, field_name in campos:
            tk.Label(formulario, text=label_text, font=("Arial", 10)).pack(pady=5)
            entry = tk.Entry(formulario, width=40)
            entry.pack(pady=5)
            entries[field_name] = entry
        
        # Si estamos editando, llenar los campos
        if producto_data:
            entries['nombre'].insert(0, producto_data[1])
            entries['descripcion'].insert(0, producto_data[2])
            entries['stock'].insert(0, producto_data[3])
            entries['precio'].insert(0, producto_data[4])
            entries['status'].insert(0, producto_data[5])
            entries['marca'].insert(0, producto_data[6])
            entries['proveedor'].insert(0, producto_data[7])
        
        def guardar_producto():
            # Obtener valores de los campos
            nombre = entries['nombre'].get().strip()
            descripcion = entries['descripcion'].get().strip()
            stock = entries['stock'].get().strip()
            precio = entries['precio'].get().strip()
            status = entries['status'].get().strip()
            marca = entries['marca'].get().strip()
            proveedor = entries['proveedor'].get().strip()
            
            # Validaciones
            if not nombre:
                messagebox.showwarning("Datos incompletos", "El nombre del producto es obligatorio.")
                return
                
            try:
                stock = int(stock) if stock else 0
                precio = float(precio) if precio else 0.0
                status = int(status) if status else 0
            except ValueError:
                messagebox.showwarning("Datos inválidos", "Stock debe ser número entero, Precio debe ser decimal y Status 1 o 0.")
                return
            
            if producto_data:  # Modo edición
                if actualizar_producto(producto_data[0], nombre, descripcion, stock, precio, status, marca, proveedor):
                    messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_productos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el producto.")
            else:  # Modo creación
                if crear_producto(nombre, descripcion, stock, precio, status, marca, proveedor):
                    messagebox.showinfo("Éxito", "Producto creado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_productos()
                else:
                    messagebox.showerror("Error", "No se pudo crear el producto.")
        
        tk.Button(formulario, text="Guardar", width=15, command=guardar_producto).pack(pady=20)
        tk.Button(formulario, text="Cancelar", width=15, command=formulario.destroy).pack(pady=5)
        
    def cerrar_sesion(self):
        self.root.destroy()
        messagebox.showinfo("Cerrar sesión", "Has cerrado sesión correctamente.")
    
    
if __name__ == "__main__":
    app = DashboardApp("admin")