
# print((a-b)**3)

# a, b, c = int(input()), int(input()), int(input())
# print(a*b*c)

# a, b = int(input()), int(input())
# Print(2* (a+b)/5)


# def obliczanienetto():
#     brutto = int(input())
#     return brutto/1.23

# print(obliczanienetto())
# print(obliczanienetto())
# print(obliczanienetto())

# def podzielnaprzez3 ():
#     a = int(input())
#     return a%3==0
# print(podzielnaprzez3())

# a = int(input())
# if a/100 >= 1:
#     print("jest podzielna")
# else:
#     print("nie jest podzielna")
# elif a%17==0:
#     print("nie jest podzielna przez 17")
# else:
#     print("jest podzielna przez 17")
# wiek = 0
# wiek = int(input("podaj wiek"))
# if wiek < 18:
#     print("nie")
# else:
#     print("tak")
# limit = int(input("podaj wage"))
# def sprawdzeniewagi():

#     return limit > 20
# print(sprawdzeniewagi("nie"))
# sprawdzeniewagi()


#bajtożabka
# p = int(input("podaj punkt startu:"))
# k = int(input("punkt końcowy:"))
# s = int(input("podaj długośc skoków:"))
# x = k - p
# if 3 * s >= x:
#     print("true ")

#zad1 
# x, y = int(input()), int(input())
# if (x + y)%2==0:
#     print("tak")
# else:
#     print("nie")

#zad2

# x, y = int(input()), int(input())
# if (x + y)/2 > (x*y)**1/2:
#     print("tak")
# else:
#     print("nie")



#zad3 

# k, l, m = int(input()), int(input()), int(input())
# if k == l or k == m or m == l:
#     print("tak")
# else:
#     print("nie")



#zad 4 
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(min(a,b,c,d))
#zad5
# k, l, m = int(input()), int(input()), int(input())
# x = (min(k,l,m))
# y = (max(k,l,m))
# if k <= l + m:
#     print("tak")
# else:
#     print("nie")


# a, b, c, = int(input("podaj a: ")), int(input("podaj b: ")), int(input("podaj c: "))
# if a < (b+c) and b < (c+a) and c< (a+b):
#   print('TAK')
# else:
#   print('NIE')


# a,b,c = int(input("podaj a = ")),int(input("podaj b = ")),int(input("podaj c = "))

# if a*a+b*b == c*c or a*a+c*c == b*b or c*c+b*b == a*a:
#     print("prostokątny")
# else:
#     if a*a+b*b < c*c or a*a+c*c < b*b or c*c+b*b < a*a:
#         print("rozwartokątny")
#     else:
#         if a*a+b*b > c*c and a*a+c*c > b*b and c*c+b*b > a*a:
#             print("ostrokątny") 


#karta3
#zad1
# n = int(input())
# for i in range(n):
#     print(i**3 + 3, end=" ")

# #kolejne

# for i in range(105,1000,15):
#     print(i, end=" ")

#pętle for liczb trzycyfrowych podzielnych przez 13
# for i in range(100, 1000):
#     if i% 13== 0:
#         print( i, end=" ")
#petle for liczb dwucyfrowych parzystych
# for i in range(10, 99, 2):
#     print( i, end=" ")

#zad1
# n = int(input())
# for i in range(n):
#     print("*-|", end=" ")

# n = int(input())
# a, b = 0, 1

# for i in range(n):
#     a, b = b, a + b
#     print(a, end=" ")


#zad2
# n = int(input())
# for i in range(1, n+1):
#     print("*"*i, end=" ")
#     if i % 2 == 1:
#         print("||", end=" ")
#     else:
#          print("--", end=" ")   

# n = int(input())
# znak = "--"
# for i in range(1, n+1):
#     print("*"*i, end=" ")
#     if znak == "--":
#         znak = "||"
#     else:
#         znak="--"

#karta3b
#zad1
# for dni in range(1, 31):
#     print(dni,end=" dzien ")

#zad2
# for i in range(1,10,2):
#     print(i**2)

#zad3 
# for i in range(1000, 10000):
#     if i%379==0:
#         print(i)
#zad4

# for i in range(101, 1000):
#     if i %5 ==0 or i %6 ==0 or i %11 ==0:
#         print(i)

#zad5

# n = int(input())
# g = 0
# for i in range(n):
#     k = int(input())
#     g += k
# print(g)

#karta4
# def f(n):
#     if n == 0:
#         return 3
#     else:
#         f(n-1)+2
# print(f(n))


# metoda herona
# def metoda_herona(p):
#     b = p
#     while abs(b-p/b) > 0.00001:
#         b = (b + p/b)/2
#     return (b + p/b)/2
# print(metoda_herona(9))

#karta5
#zad1
def suma(liczba):

    suma = 0
    for i in range(2,liczba):
        pierwsza = True
        for j in range(2,i // 2 + 1):
            if i % j == 0:
                pierwsza = False
                break
        if pierwsza:
            suma += i
    return suma
print(suma(10))

# Zad 2
# def suma_cyfr(liczba, pierwiastek):
#     iloczyn = liczba ** pierwiastek
#     suma = 0
#     while iloczyn > 0:
#         suma += iloczyn % 10
#         iloczyn //= 10
#     return suma
# print(suma_cyfr(2,2019))

















# Zad 3
# n = int(input())
# def lista_boków_trójkątów(x):
#     list = []
#     for a in range(1, x):
#         for b in range(a, x):
#             c = (a ** 2 + b ** 2) ** 0.5
#             if a + b + c == x and c == int(c):
#                 list.append((a, b, int(c)))
#     return list
# print(lista_boków_trójkątów(n))

# Zad 4
# def dzielnik(n, d):
#     return n % d == 0
# a, b = int(input()), int(input())
# print(dzielnik(a, b))

# Zad 5
# def suma_cyfr(x):
#     suma = 0
#     while x > 0:
#         suma += x % 10
#         x //= 10
#     return suma
# n = int(input())
# print(suma_cyfr(n))

# Zad 6
# Wersja 1
# def pierwsza(n):
#     if n % 2 == 0:
#         return druga(n)
#     else:
#         return trzecia(n)
# def druga(n):
#     return n * 3
# def trzecia(n):
#     return n * 0.4
# Wersja 2







































# #zad69

# def dick_draw():

#     # ayy lmao u nigga gay
#     i_want_more_dicks = 'Y'

#     # vvv this line below thinks you're all into dicks and you probably love them, which in short, makes you really gay.
#     while i_want_more_dicks == 'Y':

#         # initialize variables to be filled in with loops later.
#         shaft = '' # dick body units
#         head = '' # dickhead type/shape
#         cumshot = '' # jizz length (could be piss for you, but whatever)

#         # input dick stats.
#         dick_length = int(input('enter dick length (must be a number, enter 0 for a chode): '))
#         while dick_length < 0:
#             dick_length = int(input("i can't draw a retracted cock, you shit cunt! "))
#         dickhead = int(input('enter dickhead type\nreference: o O 0 D (type a number 1-4): '))
#         while dickhead < 1 or dickhead > 4:
#             dickhead = int(input('enter a valid dickhead type you fuckwit! '))
#         cumshot_length = int(input('enter cumshot length (must be a number, enter 0 for no jizz): '))
#         while cumshot_length < 0:
#             cumshot_length = int(input("a dick can't cum inside itself, you fucking faggot! "))

#         # phallic algorithms in work.
#         for dickflesh in range(dick_length):
#             shaft = '=' * dick_length
#         if dickhead == 1:
#             head = 'o'
#         if dickhead == 2:
#             head = 'O'
#         if dickhead == 3:
#             head = '0'
#         if dickhead == 4:
#             head = 'D'
#         for jizz_range in range(cumshot_length):
#             cumshot = '~' * cumshot_length

#         # your carefully crafted phallus is about to be provided. congratu-fucking-lations. cock successfully made.
#         print("here's your dick:\n8" + shaft + head + cumshot)

#         # if u type in yes there4 u rly gay lmao
#         i_want_more_dicks = input('do you wish to draw a dick again? enter "Y" for yes, anything else for no: ')
# dick_draw()



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



