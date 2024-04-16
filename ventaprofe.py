import os

os.system("cls")

#solicitar cantida de pasajes
#soliccitar precio de cada pasaje
#validar con try except
#total ingresos
#romper bucle con break en caso que el valor != int
#mostrar info del total de pasajes
totalingresos = 0
banderacantidad = True
banderaprecio = True
while banderacantidad:
    try:      
        cantidad = int(input("ingrese cantidad de pasajes\n"))
        for x in range(cantidad):
            while banderaprecio:
                try:
                   precio = int(input(f"ingrese precio de pasaje n° {x+1}\n"))
                   totalingresos = totalingresos+precio
                   break
                except:
                    print("precio indicado no valido")
        break            
    except:
        print("opcion no valida")

print(f"para los {cantidad} de pasajes, el valor a pagar es de: ${totalingresos}\n")
