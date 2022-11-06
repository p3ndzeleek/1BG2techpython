#zad 1 - Medium - Oblicz sumę k początkowych liczb  trzycyfrowych
# 100 + 101 + 102 + 103 ...

# k = int(input())
# suma = 0
# for i in range(100,100 + k):
#     suma = suma + i
# print(suma)
# Zad 2 - Hard - Oblicz sumę n początkowych wyrazów ciągu fibonacciego
# 1 + 2 + 3 + 5 + 8 + 13 ....
# n = int(input())
# a, b = 1, 0
# suma = 0
# for i in range(n):
#     a, b = b, a+b
#     suma = suma + b
# print(suma)

# Zad 3 - Hard - Spradź czy liczba wpisana przez usera jest doskonała
# doskonała to taka, która jest równa sumie swoich dzielników bez niej samej
# 6 = 1 + 2 + 3 (JEST)
# 10 = 1 + 2 + 5 (NIE JEST)
# 28 = 1 + 2 + 4 + 7 + 14 (JEST)

# n = int(input())
# suma = 0
# for i in range(1,n):
#     if n %i ==0:
#         suma =+ i
# if suma ==n:
#     print("tak")
# else:
#     print("nie")

# Zad 4 - Medium - Oblicz sumę liczb dwucyfrowych parzystych podzielnych przez 7
# Sprawa oczywista :)

# for i in range(10, 100, 2):
#     if i %7 ==0:
#         print()

