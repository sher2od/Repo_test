from num2words import num2words
son = int(input("Pulni kiriting >> "))

k_50 = son // 50
son = son % 50
print(f"$50 kupuradan ",k_50 ,"ta")

k_10 = son // 10
son = son % 10
print(f"$10 kupyuradan",k_10,"ta")

k_5 = son // 5
son = son % 5
print(f"$5 kupuradan",k_5,"ta")

k_1 = son // 1
son = son % 1
print(f"$1 kuouryadan ", k_1,"ta")

son1 = 186
print("umumiy summa >",son1)
print(num2words(son1,len='en'))
print(num2words(son1,len='ru'))

