from num2words import num2words

mahsulot_q = input("haftalik mahsulotni kiriting vergul bilan  >> ")
bosh = 0
for i in mahsulot_q.split(","):
    bosh += float(i)
j = bosh / 7

print(f"ortacha xarajat {j:.2f}")
print(num2words(j,lang="en",to = 'currency'))
print(num2words(j,lang="ru",to = 'currency'))


