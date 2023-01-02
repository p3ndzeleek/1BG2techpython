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

# for i in range(99, 9, -1):
#     if i %7 == 0:
#         podzielnik = i
#         break
# ilosc = 0
# for i in range(1000,10000):
#     if i % podzielnik == 0:
#         ilosc += 1
# print(ilosc)

# #zad4
# for i in range(10,100):
#     cd = i // 10
#     cj = i % 10
#     if cd >= 2*cj:
#         ilosc += 1
# print(ilosc)

#zad5
# for i in range(100,1000)       
# print((i % 100)//10)

#zad6

# n = int(input())

#opcja1

# licznik = 0
# suma = 0 
# i = 10
# while True:
#     if i % 19 ==0:
#         suma += i
#         licznik+= 1
#     if licznik == n:
#         break
#     i += 1
# print(suma)
    
#opcja2

# licznik = 0
# suma = 0
# for i in range(10,100):
#     if i %19==0:
#         suma += i
#         licznik += 1
#     if licznik == n:
#         break
# print(suma)

#opcja3
# suma = 0
# for i in range(19,19*n+1,19):
#     suma += i
# print(suma)

#opcja4

# suma = 0
# for i in range(1,n+1):
#     suma = suma +19*i
# print(suma)


#zad7
# n = int(input())
# suma = 0
# for i in range(999-(999%37), 999-(999%37)-(37*n), -37):
#     suma += i 
# print(suma)

# n = int(input())
# suma = 0
# licznik = 0
# for i in range(999,99,-1):
#     if i %37==0:
#         suma +=i
#         licznik += 1

#zad8
# n = int(input())
# x = 5
# suma = 2
# for i in range(1,n+1):
#     suma += x
#     x = (abs(x) + 3)*(-1) ** i
#     print(suma)

# Zad 9
# n = int(input())
# il = 1
# x = 1
# for i in range(n):
#     il = il * x
#     x *= -2
# print(il)

# Zad 10
# n = int(input())
# suma = 0
# for i in range(1, n + 1):
#     il = 1
#     for i in range(1, i + 1):
#         il = il * i
#     suma += il
# print(suma)

# Zad 11
# n = int(input())
# a = 1
# suma = 0
# for i in range(1, n + 1):
#     b = i * i
#     suma += a/b
#     a += 2
# print(suma)

# Zad 12
# n = int(input())
# a = 1
# suma = 0
# sumb = 0
# for i in range(1, n + 1):
#     suma += a
#     a += 2
#     b = i * i
#     sumb += b
# print(suma/sumb)

# Zad 13
# n = int(input())
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2
# print(suma)

# Zad 14
# n = int(input())
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2
# print(suma)

# Zad 15
# n = int(input())
# a = 3
# b = 1
# il = 1
# for i in range(n):
#     il *= a/b
#     a += 1
#     b = b * 2 + 1
# print(il)

# Zad 16
# n = int(input())
# a1 = 1
# a2 = 2
# b = 1
# il = 1
# for i in range(1, n + 1):
#     il *= a1/b
#     a1, a2 = a2, a1 + a2
#     b *= 2
# print(il)