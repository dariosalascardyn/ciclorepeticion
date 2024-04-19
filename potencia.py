base0 = int(input("ingrese el valor de la base\n"))

flag = base0
while base0 <= 0:
  print("la base debe ser mayor a 0")
  base0 = int(input("ingrese el valor de la base\n"))


exponente0 = int(input("ingrese valor exponente\n"))

while exponente0 <=0:
    print("el exponente debe ser mayor a 0")
    exponente0 = int(input("ingrese valor exponente\n"))
  
resultado = 1
for x in range(exponente0):
  resultado = base0 * resultado

print(f"el resultado potencia de base {base0}, y exponente {exponente0}, es igual a {resultado}")

