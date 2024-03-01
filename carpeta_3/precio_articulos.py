# entrada
precio_costo = float(input("Ingrese el precio de costo: "))

# proceso
if precio_costo < 3000:
    print("El precio de venta es: ", precio_costo*15/100 + precio_costo)
elif precio_costo > 6000:
    print("El precio de venta es: ", precio_costo*25/100 + precio_costo)
else:
    print("El precio de venta es: ", precio_costo + 500)
