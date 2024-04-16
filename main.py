import os

os.system("cls")

#ciclo repeticion for -> para
# for x in range(3):
#     print(f"se portaron mal el sabado {x}")

# contadorNota = 0
# try:
#     cantidad = int(input("ingrese cantidad de notas a promediar\n"))
#     for x in range(cantidad):
#         nota = float(input(f"ingrese nota {x+1} \n"))
#         contadorNota = contadorNota + nota
#     promedio = contadorNota/cantidad  #round(contadorNota/cantidad, 1)  
#     promedioRedondeado = round(promedio, 1)
#     print(f"el resultado de las {cantidad} notas es: {promedioRedondeado}")
# except:
#     print("tipo de dato no es compatible")


# WHILE -> Mientras
bandera = True

while bandera :
    numero = int(input("ingrese un numero\n"))
    if numero%2==0 :
        print("puede elegir otro numero!")
    else:
        print("el numero es impar, se acabo el ciclo")
        #bandera = False
        break
    
print("muchas gracias por ocupar esta gran aplicación")


a = 10
while a >= 10:
    a = int(input("ingrese numero\n"))
print("baicito")
