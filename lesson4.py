from num2words import num2words



km = input("Manzilgacha nechi km? >> ")
y_km = float(km)
summa = 3.00 + (y_km * 1.20)
print(num2words(summa,lang= 'en'))
print(num2words(summa,lang= 'ru'))
