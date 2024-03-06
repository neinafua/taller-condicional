# entrada
m= float(input("cuantos metros cúbicos de agua consumio en el mes: "))
# proceso
cuota_fija = 10000
cuota_metro_50_200 = 2000
cuota_metro_200_mas = 3000
if m<=50:
    print("tiene que pagar $10000")
elif m<200:
    print("tiene que pagar" + "$" +str(cuota_fija + cuota_metro_50_200))
else:
    print("tiene que pagar" + "$" +str(cuota_fija + cuota_metro_200_mas))

