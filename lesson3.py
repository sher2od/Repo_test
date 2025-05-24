from num2words import num2words

mahsulot_q = input("haftalik mahsulotni kiriting vergul bilan  >> ")
bosh = 0
for i in mahsulot_q.split(","):
    bosh += float(i)
summa = bosh / 7

dollar = int(summa)
cents = int(round((summa - dollars) * 100))


summa_en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
summa_ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центa"

print(f"Yetkazib berish narxi: ${summa:.2f} ({summa_en}, {summa_ru})")


