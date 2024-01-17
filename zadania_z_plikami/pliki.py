with open("owoce.txt", "r" ) as plik:
    lista_owocow = file.read().splitlines()

print(lista_owocow)
a,b,c,d,e,f = lista_owocow
print(a)

for i in lista_owocow:
    print(i)

for i in range(len(lista_owocow)):
    print(i, lista_owocow[i])

print(lista_owocow[0])
print(lista_owocow[1:3])


