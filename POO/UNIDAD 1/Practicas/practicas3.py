# Practica 3. introduccion al poliformismo

# Simular un sistemas de cobro de almenos 4 tipos.

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de $ {cantidad} con tarjeta de debito/crédito."

class pago_efectivo:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de $ {cantidad} en efectivo."
    
class pago_paypal:
    def procesar_pago(self, cantidad):
        nombre = input("Ingrese su nombre de usuario de PayPal: ")
        return f"Procesando pago de $ {cantidad} a través de PayPal para el usuario {nombre}."
    
class pago_transferencia:
    def procesar_pago(self, cantidad,):
        cantidad_total = cantidad + 20
        return f"Procesando pago de $ {cantidad_total} mediante transferencia bancaria (incluye comisión de $20)."  
    
metodo_pago = [pago_tarjeta(), pago_efectivo(), pago_paypal(), pago_transferencia()]

for m in metodo_pago:
    print(m.procesar_pago(100)) 
    
    
#ACTIVIDAD 1 
#PROCESAR DIFERENTES CANTIDADES EN CADA OPCION DE PAGO: 100 con tarjeta, 5000 en efectivo, 400 con paypal y 600 con transferencia bancaria.

pago1 = pago_tarjeta()
print(pago1.procesar_pago(100))
pago2 = pago_efectivo()
print(pago2.procesar_pago(5000))
pago3 = pago_paypal()
print(pago3.procesar_pago(400))
pago4 = pago_transferencia()
print(pago4.procesar_pago(600))


#Actividad 2. adicional a megtodo procesar_pago() cuando sea transferencia: sumar 20(comicion) a cantidad.
#Cuando sea paypal, pedirle al usuario su nombre.


