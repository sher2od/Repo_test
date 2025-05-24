from num2words import num2words




m = float(input("Manzilgacha nechi km (Boshlangich tolov $3.00) >> "))


summa = round(3.00 + (m * 1.20), 2)  


dollars = int(summa)
cents = int(round((summa - dollars) * 100))


summa_en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
summa_ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центa"


print(f"Yetkazib berish narxi: ${summa:.2f} ({summa_en}, {summa_ru})")
