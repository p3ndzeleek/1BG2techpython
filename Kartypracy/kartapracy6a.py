# Zad 1
# x = int(input())
# suma = 0
# while x > 0:
#     suma += x % 10
#     x //= 10
# print(suma)

# Zad 2
# a = int(input())
# for i in range(2, int(a ** 0.5) + 1):
#     if a % i == 0:
#         print("NIE")
#         exit(0)
# print("TAK")

# Zad 3
# a = int(input())
# suma = 0
# for i in range(1,(a // 2) + 1):
#     if a % i == 0:
#         suma += i
# if suma == a:
#     print("TAK")
# else:
#     print("NIE")

#zad4
# x = int(input())
# y = int(input())
# while x > 0:
#     y, x=x, y%x
# if x == 1:
#     print("Tak")
# else:
#     print("Nie")

#zad5

m = int(input())
for i in range(10,20):
    x, y =i, m
    while y>0:
        x, y = y , x%y
    if x ==1:
        print(f"TAK{i} i {m} sa względne")
    else:
        print(f"NIE, {i} i {m} nie sąwzględne")