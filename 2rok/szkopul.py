#Zad2
# Przestępność
# Limit pamięci: 32 MB

# Mamy dany rok . Powiemy, że rok jest przestępny, gdy wartość jest podzielna przez 4. Jeśli jednak wartość dzieli się przez 100, a nie dzieli się przez 400 to rok nie jest przestępny. Zadaniem Twojego programu jest stwierdzenie czy dany rok jest przestępny.
# Zadanie

# Napisz program, który:

#     wczyta ze standardowego wejścia liczbę naturalną oznaczającą rok,
#     wypisze TAK jeśli rok jest przestępny, albo NIE jeśli nie jest.

# Wejście

# Jedna liczba naturalna oznaczającą rok.
# Wyjście

# W jedynym wierszu wyjścia należy wypisać TAK jeśli rok jest przestępny, albo NIE jeśli nie jest.
# Przykład

# Dla danych wejściowych:

# 1066

# poprawną odpowiedzią jest:

# NIE

# year = int(input())
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("TAK")
# else:
#     print("NIE")


#zad3
