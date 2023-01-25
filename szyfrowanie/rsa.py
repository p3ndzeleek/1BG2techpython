#pre najwiekszy wspolny dzielnik
# from math import gcd
# print(gcd(15,20))

#wybór 2 duzych liczb pierwszych 

p = 101
q = 97


#2 liczbym n = p * q oraz funkcje eulera F = (p-1) * (q-1)
n = p * q
F = (p - 1) * (q - 1)
print(n)
print(F)

#3 generujemy klucz publiczny e taki, ze NWD(F,e) = 1

from math import gcd
for i in range(2,F):
    if gcd(i,F) == 1:
        e = i 
        break
print(e,n)

# 4 generujemyklucz prywatny d : d * e mod F = 1
for j in range(2,F):
    if ((j * e)%F)==1:
        d = j
        break
print(d,n)
#5 jak szyfrowac?
#mamy m - widomośc
# c = m**e%n ( c - cipher - szyfrogram,tekst zaszyfrowany)
#t = c ** d % n (t - text - tekst jest jawny)

m = input()
cipher = ""
for i in m:
    cipher += chr((ord(i)**e)%n)
print(m)
print(cipher)

tekst = ""
for i in cipher:
    tekst += chr((ord(i)**d) % n )
print(tekst)