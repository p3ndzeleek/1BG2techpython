# a,b,c =int(input()), int(input()), int(input()),
# #ciąg arytmetyczny 
# if a - b == b - c:
#     print("ciąg jest arytmetyczny")
# else:
#     print("ciąg nie jest arytmetyczny")
# #ciaggeomertyczny
# if a / b == b / c:
#     print("jestgeometryczny")
# else:
#     print("niejestgeometryczny")
# #rosnący 
# if a < b < c:
#     print("jest rosnący")
# else:
#     print(" nie jest rosnący")
# #malejący
# if a > b > c:
#     print("jestmalejący")
# else:
#     print("niejestmalejący")

#zad2

# suma = 0
# for i in range(100, 1000):
#     if i %8 == 0 and i %16 !=0:
#         suma += i
# print(suma)

#zad3

for i in range(99, 9, -1):
    if i %7 == 0:
        podzielnik = i
        break
ilosc = 0
for i in range(1000,10000):
    if i % podzielnik == 0:
        ilosc += 1
print(ilosc)


