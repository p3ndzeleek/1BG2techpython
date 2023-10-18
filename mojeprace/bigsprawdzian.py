 #1 wstęp
# oblicz sume liczb 3 cyfrowych 
# suma = 0
# for i in range (100, 1000):
#   suma += i
# print ("suma wynosi ",  suma ) 

# # Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
# suma = 0 
# ilość = 0 
# for i in range (6, 1000):
#   if i % 6 == 0:
#     suma += i 
#     ilość += i 
# print ("suma, " , suma )
# print ("ilosc ,", ilość  )

# # Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
# from random import randint
# L = (randint(1000,9999) for i in range (5))
# #print (L)
# największa = max(L)
# print (największa )

# #Podaj sumę cyfr w dowolnej liczbie
# suma = 0 
# a = int(input())
# for i in str(a):
#     suma += int(i)
# print("Suma cyfr w liczbie", a, "to:", suma)

# #Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
# a = input("podaj liczbe 3 cyfrową " )
# if len(a) == 3 :
#   najmniejsza = min(a)
#   print("Najmniejsza cyfra w liczbie", a, "to:", najmniejsza)
# else :
#   print ("jesteś debilem miała byc 3 cyfrowa ")

# # Sprawdź czy wpisana przez usera liczba jest pierwsza
# n = int(input())
# for i in range (2, n ):
#   if n % i == 0 :
#     print("lizcba nie jest pierwsza ")
#     exit(0)
# print("liczba jest pierwsza")

# #Sprawdź czy wpisana przez usera liczba jest złożona
# n = int(input())
# for i in range (2, n ):
#   if n % i != 0 :
#     print("lizcba nie jest złożona ")
#   else :
#     print("liczba jest złożona")
#   exit(0)

# #Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24 
# from math import gcd 
# a = int(input())
# liczba = 24 
# if gcd (a, liczba) == 1 :
#   print ("jest względnie pierwsza")
# else:
#   print("nie jest względnie pierwsza")

# #Zakoduj szyfrem CEZARA i kluczem k słowo s.
# napis = input("Podaj napis do szyfracji: ")
# szyfr = ""
# klucz = int(input("Podaj klucz: "))

# for i in range(len(napis)):
#     szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + klucz) % 26)
# print("Szyfracja:", szyfr)

# #Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę m
# from math import gcd 
# a = int(input("gora pierwszego ulamka "))
# b = int(input("dol pierwszego ulamka "))
# c = int(input("gora drugiego ulamka "))
# d = int(input("dul drugiego ulamka "))
# #dodoajemy  licznik 
# licznik = a *d + c*b 
# mianownik = b*d 
# #skracanie 
# nwd = gcd(licznik, mianownik)
# licznik = licznik // nwd
# mianownik = mianownik // nwd
# print(licznik, "/", mianownik)

# #Znajdź NWW dwóch wpisanych przez usera liczb
# from math import gcd
# liczba1 = int(input("Wpisz pierwszą liczbę: "))
# liczba2 = int(input("Wpisz drugą liczbę: "))
# nwd = gcd(liczba1, liczba2)
# nww = (liczba1 * liczba2) // nwd
# print("Najmniejsza wspólna wielokrotność (NWW):", nww)

# # - NAPISY
# # Znajdź ilość liter C we wpisanym napisie
# n = input()
# c = n.count("C")
# print(c)

# #Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
# napis = input("Podaj napis: ")
# nierosnacy = True
# for i in range(1, len(napis)):
#     if ord(napis[i]) > ord(napis[i - 1]):
#         nierosnacy = False
#         break
# if nierosnacy:
#     print("Litery w napisie są w porządku nierosnącym.")
# else:
#     print("Litery w napisie nie są w porządku nierosnącym.")


# #Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
# a = input("Wprowadź pierwszy wyraz: ")
# b = input("Wprowadź drugi wyraz: ")
# c = input("Wprowadź trzeci wyraz: ")

# dlugosc1 = len(a)
# dlugosc2 = len(b)
# dlugosc3 = len(c)

# if dlugosc1 > dlugosc2 and dlugosc1 > dlugosc3:
#     print("Najdłuższy wyraz to 1:", a)
#     print("Długość:", dlugosc1)
# elif dlugosc2 > dlugosc1 and dlugosc2 > dlugosc3:
#     print("Najdłuższy wyraz to 2:", b)
#     print("Długość:", dlugosc2)
# elif dlugosc3 > dlugosc1 and dlugosc3 > dlugosc2:
#     print("Najdłuższy wyraz to 3:", c)
#     print("Długość:", dlugosc3)
# else:
#     print("Wyrazy mają taką samą długość.")

# print("NWD odejmowanie")
# a = int(input("Podaj 1 liczbę: "))
# b = int(input("Podaj 2 liczbę: "))
# while a != b :
#     if a > b :
#         a -= b
#     else :
#         b -= a
# print("NWD", a)

# # NWD
# a = int(input())
# b = int(input())
# while b>0:
#   a, b = b, a%b
#   print (a)