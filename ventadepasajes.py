import os

os.system("cls")

#contadorpasajes = 0
while true:
    try:
        cantpasajes = int(input("ingrese cantiddad de pasajes que desea vender:\n"))
        if cantpasajes >= 0:
            print(f"cantidad de pasajes a vender: {cantpasajes}\n")  
        else:
            print("cantidad no valida, ingrese denuevo porfavor:\n")
    except:
            print("valor no valido")

# # Función para solicitar la cantidad de pasajes al usuario
# def solicitar_cantidad_pasajes():
#     while True:
#         try:
#             # Pedimos al usuario que introduzca la cantidad de pasajes
#             cantidad = int(input("Por favor, ingresa la cantidad de pasajes que deseas vender: "))
#             # Verificamos que la cantidad sea un número positivo
#             if cantidad >= 0:
#                 return cantidad
#             else:
#                 print("Por favor, ingresa un número positivo.")
#         except ValueError:
#             # Manejo de error si el usuario no ingresa un número
#             print("Por favor, ingresa un número válido.")

# # Usamos la función y guardamos la cantidad de pasajes
# cantidad_pasajes = solicitar_cantidad_pasajes()
# print(f"Cantidad de pasajes a vender: {cantidad_pasajes}")
