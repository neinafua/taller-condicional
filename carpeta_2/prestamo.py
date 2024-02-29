# entrada
salario = int(input("Ingrese su salario: "))
deuda = (input("tiene alguna deuda antigüa?: "))

# proceso
if salario >= 945200:
    if deuda == "no":
        print("Puede solicitar el prestamo")
    else:
        print("No puede solicitar un prestamo")
elif salario < 945200:
    print("No puede solicitar un prestamo")
    