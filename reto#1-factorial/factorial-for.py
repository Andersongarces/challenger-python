# Encontrar el factorial de un numero 
# Eres una rata si usas la libreria Math 

numero = int(input("ingrese el numero: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")





