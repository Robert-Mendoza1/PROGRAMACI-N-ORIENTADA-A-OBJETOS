#Practica diagnostico_nombre.py
#Simulador de ticket de venta
#Objetivo: aplicar funciones, bucles, condiciones
#listas y variables

#elegir una tematica deun negocio que vende 3 productos

productos = ["Camiseta", "Pantalon", "Zapatos"]
precios = [150, 250, 450]

#Funcion para calcular el total 
def calcular_total(cantidades, precios):
    total = 0
    for i in range (len(cantidades)):
        total += cantidades[i] * precios[i]
        return total
    
#menu de ususario
def menu():
    print("Bienvenido a la tienda de ropa")
    nombre = input("Por favor, ingrese su nombre: ")
    
    cantidades = []
    print("Selecciona el producto que deseas comprar:")
    for i in range (len(productos)):
        print (f"{i+1}. {productos[i]} - ${precios[i]}")
        cantidad = int(input(f"¿Cuántas {productos[i]} deseas comprar? "))
        cantidades.append(cantidad)
    total = calcular_total(precios, cantidades)
    print(f"{nombre}, el total de tu compra es: ${total}")
    print("Gracias por tu compra. ¡Vuelve pronto!")
menu()
