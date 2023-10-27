#zad1
# def FizzBuzz(n):
# 	if n % 3 == 0 and n % 5 == 0:
# 		return "Fizz Buzz"
# 	elif n % 3 == 0:
# 		return "Fizz"
# 	elif n % 5 == 0:
# 		return "Buzz"
# 	else:
# 		return str(7)

# print(FizzBuzz(5))
# print(FizzBuzz(3))
# print(FizzBuzz(15))
# print(FizzBuzz(7))
# #zad2
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='\t')
#     print()
#zad3
# def lata_20 (start_rok):
#     years = []
#     for i in range(start_rok, start_rok + 20):
#         years.append(i)
#     return years

# print(lata_20(2024))
# def lata_przestepne():
#     przestepne_rok = []
#     for rok in range(2024, 1581, -1):
#         if rok % 4 == 0:
#             if rok % 100 == 0:
#                 if rok % 400 == 0:
#                     przestepne_rok.append(rok)
#             else:
#                 przestepne_rok.append(rok)
#     return przestepne_rok

# print(lata_przestepne())

def lata_przestepne():
    przestepne_rok = []
    for rok in range(2024, 1581, -1):
        if rok % 4 == 0:
            if rok % 100 == 0:
                if rok % 400 == 0:
                    przestepne_rok.append(rok)
            else:
                przestepne_rok.append(rok)
    return przestepne_rok

przestepne = lata_przestepne()
for rok in przestepne:
    print(rok)

