
# #ord() zwraca kod ascii danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("C"))
# #chr() zwraca zak danego kodu ascii
# print(chr(65))
# print(chr(75))
# print(chr(89))

#wypisanie alfabetu
# for i in range(65, 91):
#     print(chr(i), end="")

napis = "POLSKA"
# print(len(napis)) #zawraca długość napisu
# print(napis[0]) #napis to lista
# print(napis[1])
# print(napis[2])

for i in range(len(napis)):
    print(chr(65+ord(napis[i]-65+3)%26))


