# Reto #0 - Convertir de Euro a dolar

euros_ingresados = input("Ingresa la cantidad en euros: ")

if euros_ingresados.replace(".", "", 1).isdigit():
    euros_ingresados = float(euros_ingresados)

    tipo_cambio = 1.09

    dolares_convertidos = round(euros_ingresados * tipo_cambio, 2)
    
    print(f"{euros_ingresados} euros son aproximadamente {dolares_convertidos} dólares.")
else:
    print("Por favor, ingresa una cantidad válida en euros.")

