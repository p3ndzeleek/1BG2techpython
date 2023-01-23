#Wygeneruj tablicę n losowych liczb:
# from random import randint
# L = [randint(1,20) for i in range(20)]



#1. Znajdź największą liczbę w tablicy
#2. Znajdź najmniejszą liczbę w tablicy
#3. Podaj ile razy występuje najwieksza liczba w tablicy
#4. Podaj ile razy występuje najmniejsza liczba w tablicy
#5. Podaj rozpiętość tablicy (różnica max - min)
#6. Podaj sumę liczb w tablicy
#7. Podaj średnią wartość liczb w tablicy
#8. Których liczb jest więcej w tablicy: parzystych czy nieparzystych?
#9. Ile w tablicy jest liczb pierwszych?
#10. Podaj v-ce max i v-ce min liczb tablicy

#losowa tablica
from random import randint
L = [randint(1,20) for i in range(20)]

print(f"lista: {L}")

#zad1
print(max(L))

#zad2
print(min(L))

#zad3
print(L.count(max(L)))

#zad4
print(L.count(min(L)))

#zad5
print(max(L)-(min(L)))

#zad6
print(sum(L))

#zad7
print(sum(L)//(count(L)))