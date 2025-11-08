from database import crear_conexion

def ver_productos():
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        query = "SELECT id_producto, nombre_producto, description, stock, precio, status, marca, provedor FROM productos"
        cursor.execute(query)
        
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
    return []

def crear_producto(nombre_producto, description, stock, precio, status, marca, provedor):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO productos (nombre_producto, description, stock, precio, status, marca, provedor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre_producto, description, stock, precio, status, marca, provedor))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear producto: {e}")
        return False
    
def actualizar_producto(producto_id, nombre_producto, description, stock, precio, status, marca, provedor):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "UPDATE productos SET nombre_producto = %s, description = %s, stock = %s, precio = %s, status = %s, marca = %s, provedor = %s WHERE id_producto = %s"
        cursor.execute(query, (nombre_producto, description, stock, precio, status, marca, provedor, producto_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return False
    
def eliminar_producto(producto_id):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id_producto = %s"
        cursor.execute(query, (producto_id,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        return False