import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenidos {username}")
        self.root.geometry("600x400")   
        self.root.resizable(False, False)
        
        
        self.crear_elementos()
        self.root.mainloop()
        
    def crear_elementos(self):
        tk.Label(self.root, text=f"¡Bienvenido al Dashboard, {self.username}!", font=("Arial", 16, "bold")).pack(pady=10)
        
        tk.Button(self.root, text="Ver usuarios del sistema", width=20, command=self.ver_usuarios).pack(pady=20)
        
        tk.Button(self.root, text="Agregar nuevo usuario", width=20, command=self.agregar_usuario).pack(pady=10)
        
        tk.Button(self.root, text="Actualizar usuario", width=20, command=self.actualizar_usuario).pack(pady=10)
        
        tk.Button(self.root, text="Cerrar sesión", width=20, command=self.cerrar_sesion).pack(pady=30)
        
        
    def ver_usuarios(self):
        messagebox.showinfo("Lista de usuarios", "Funcionalidad para ver usuarios del sistema.")
        
    def agregar_usuario(self):
        messagebox.showinfo("Agregar usuario", "Funcionalidad para agregar un nuevo usuario.")
    
    def actualizar_usuario(self):
        messagebox.showinfo("Actualizar usuario", "Funcionalidad para actualizar un usuario existente.")
        
    def cerrar_sesion(self):
        self.root.destroy()
        messagebox.showinfo("Cerrar sesión", "Has cerrado sesión correctamente.")
    
    
if __name__ == "__main__":
    app = DashboardApp("admin")