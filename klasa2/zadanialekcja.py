# liczba  = [random.uniform(0,50) for i in range (20)]
# print("Tablica liczb ", liczba)

# nieparzysta = any(liczba % 2! = 0 for liczba in liczba)
# print(nieparzysta)


# #do tabeli 6 owocow - pytajac sie za kazdym razem uzytkownika o jego ulubiony owoc
# owoce = []
# for i in range(6):
#     owoce1 = input("Podaj ulubiony owoc: ")
#     owoce.append(owoce1)

# #w nowej tabeli wypisz ile ma znakow kazdy z owocow

# dlugosc = [len(owoc) for owoc in owoce]
# print(owoce, dlugosc)


year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("TAK")
else:
    print("NIE")