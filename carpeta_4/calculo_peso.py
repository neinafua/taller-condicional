# entrada
peso = float(input('cual es su peso: '))
altura = float(input('cual es su altura: '))

#proceso
IMC = peso/ altura**2

if IMC < 16:
    print('criterio de ingreso en hospital')
elif IMC <= 17:
    print('infrapeso')
elif IMC <= 18.5:
    print('bajo peso')
elif IMC <= 25:
    print('peso normal (saludable)')
elif IMC <= 30:
    print('sobrepeso(obesidad de grado I)')
elif IMC <= 35:
    print('sobrepeso crónico(obesidad de grado II)')
elif IMC <= 40:
    print('obesidad premórbida(obesidad de grado III)')
elif IMC > 40:
    print('obesidad mórbida(obesidad de grado IV)')
print('su IMC es: ', IMC)
