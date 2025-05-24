oy_b = float(input("Oy boshidagi korsatgich >> "))
oy_o = float(input("Oy oxiridagi kotsatgich >> "))

summa = raund((oy_o - oy_b) * 0.45,2)
dollars = int(summa)
cents = int(round((summa - dollars) * 100))


summa_en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
summa_ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центa"


print(f"Tolov: ${summa:.2f} ({summa_en}, {summa_ru})")
