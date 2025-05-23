from num2words import num2words

m_narxi = input("Mahsulot narxlarini kiriting (vergul bilan): ")
n = 0

for m in m_narxi.split(","):
    n += float(m)  # Stringni floatga aylantirish va jamlash

print(f"Jami: ${n:.2f}")
print("Inglizcha:", num2words(n, lang='en'))
print("Ruscha:", num2words(n, lang='ru'))
