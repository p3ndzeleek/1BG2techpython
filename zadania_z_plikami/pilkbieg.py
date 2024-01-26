# with open("bieg.txt", "r") as plik:
#     dane = [map(int,i.split()) for i in plik]

# #dane
# for i in range(len(dane)):
#     # a,b = map(int,dane[i])
#     a,b = dane[i]
#     # a,b = int(a), int(b)
#     if a> b:
#         print("tak trzymaj")
#     else:
#         print("nie trzymaj")


year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("TAK")
else:
    print("NIE")