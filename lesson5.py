from num2words import num2words

# Foydalanuvchidan masofa olish
m = float(input("Masofani kiriting (Boshlang‘ich to‘lov $5.00) >> "))

# Narxni hisoblash
summa = round(5.00 + (m * 0.80), 2)  # ikkita kasr raqamga yaxlitladik

# Dollar va centlarga ajratish
dollars = int(summa)
cents = int(round((summa - dollars) * 100))

# So‘zda ifoda (Inglizcha va Ruscha)
summa_en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
summa_ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центов"

# Natijani chiqarish
print(f"Yetkazib berish narxi: ${summa:.2f} ({summa_en}, {summa_ru})")
