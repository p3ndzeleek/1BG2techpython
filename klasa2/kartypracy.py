
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
# def suma(liczba):

#     suma = 0
#     for i in range(2,liczba):
#         pierwsza = True
#         for j in range(2,i // 2 + 1):
#             if i % j == 0:
#                 pierwsza = False
#                 break
#         if pierwsza:
#             suma += i
#     return suma
# print(suma(10))
 
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



# #karta6
# #zad1
# a,b,c =int(input()), int(input()), int(input()),
# #ciąg arytmetyczny 
# if a - b == b - c:
#     print("ciąg jest arytmetyczny")
# else:
#     print("ciąg nie jest arytmetyczny")
# #ciaggeomertyczny
# if a / b == b / c:
#     print("jestgeometryczny")
# else:
#     print("niejestgeometryczny")
# #rosnący 
# if a < b < c:
#     print("jest rosnący")
# else:
#     print(" nie jest rosnący")
# #malejący
# if a > b > c:
#     print("jestmalejący")
# else:
#     print("niejestmalejący")





# def suma(a, b):
#     sum = a + b
#     if sum % 2 == 0:
#         return "parzysta"
#     else:
#         return "nieparzysta"
# print(suma(2,4))



#zad 1 lampki podłączone są szeregowo. Jeśli, któraś nie działa to nie działa cały lampkowy łańcuch. Sprawdź w tabeli 20 elementowej wypełnionej 0 lub 1 (opcjonalnie False True), reprezentującej łańcuch lampkowy.
#Policz ile jest lampek działających a ile nie - 0/False - nie działają
#Zamień wszystkie 0 na 1.
# import random


# def lampki(n):
#   tab = []
#   for i in range(n):
#     tab.append(random.randint(0, 1))
#   print(tab)
#   running = 0
#   notrunning = 0
#   for i in tab:
#     if i == 1:
#       running += 1
#     else:
#       notrunning += 1

#   for i in range(len(tab)):
#     if tab[i] != 1:
#       tab[i] = 1
#   print(f"{running} działających i {notrunning} niedziałającyhch")
#   print(tab)


lampki(10)

























#zad 2 W tym roku św. Mikołaj związał worek łańcuchem na kod. Aby otworzyć kod trzeba dwa razy podać ten sam kod. Poproś o wpisanie kodu, i ponowne wspisanie i wyświetl "Kod jest poprawny - worek otwarty" jeśli kody się zgadzają lub "próbuj jeszcze raz". Można trzy razy spróbować otworzyć worek - za trzecim razem pojawia się komunikat "Do siego roku"


# def worekmikolaja():
#   licznik = 0
#   limit = 3
#   while licznik < limit:
#     licznik += 1
#     kod1 = input("podaj kod ").lower()
#     kod2 = input("podaj kod ponownie ").lower()
#     if kod1 == kod2:
#       print("Kod jest poprawny - worek otwarty")
#       break
#     elif licznik != limit:
#       print("próbuj jeszcze raz")
#     else:
#       print("Do przyszłego roku")


#zad 3 Narysuj choinkę

# from colorama import Fore


# def draw_christmas(n):
#   for i in range(1, n):

#     print(" " * (2 * n - i), end="")
#     for _ in range(2 * i - 1):
#       if 2 * i - 1 == 1:
#         print(Fore.RED + "*", end="")
#       else:
#         print(Fore.GREEN + "*", end="")
#     print()
#   print(Fore.YELLOW + " " * (2 * n - 1), end="|")


# draw_christmas(11)

#zad 4 Czy zasługujesz na prezenty  św. Mikołaja? Program pyta się "czy w Twoich oczach zasługujesz na prezent?" Jeśli odpowiedź jest nie (bez względu na wielkość liter) - to program "Do zobaczenia za rok"kończy zadanie,jeśli tak (bez względu na wielkość liter) to program pyta się jakiego rodzaju chcesz dostać prezent - wybierz ten, który chcesz dostać najbardziej: 1. kosmetyki, 2. ubrania, 3. gry 4. książki, 5. elektronikę, 6. inne. Program wypisuje:

# (*) Wynik zapisuje to pliku domikolaja.txt


# def czy_prezenty():
#   dict = {
#       1: 'kosmetyki',
#       2: "gry",
#       3: "gry",
#       4: "książki",
#       5: "elektronikę",
#       6: "inne"
#   }
#   present = input("czy w Twoich oczach zasługujesz na prezent? ").lower()
#   if present == "tak":
#     co_dostac = int(
#         input('''Co chcesz dostać?
# 1. kosmetyki, 
# 2. ubrania, 
# 3. gry 
# 4. książki, 
# 5. elektronikę, 
# 6. inne.'''))
#     print(f"Na prezent dostaniesz {dict.get(co_dostac, 0)}")
#   else:
#     print("Do zobaczenia za rok")


# czy_prezenty()

#zad 5
# ile zostało dni do Wigilii - 24.12. *do końca nauki w tym roku

# from datetime import datetime


# def dni_do_Wigilii():
#   dzisiaj = datetime.now()
#   #tutaj ustawiam datę
#   wigilia = datetime(dzisiaj.year, 12, 24)
#   if dzisiaj > wigilia:
#     wigilia = datetime(dzisiaj.year, 12, 24)
#   pozostalo = wigilia - dzisiaj
#   return pozostalo.days  #bez tego days z godzinami daje


# print(f"Do wigilii zostało {dni_do_Wigilii()} dni")


# def dni_do(month, day):
#   dzisiaj = datetime.now()
#   #tutaj ustawiam datę
#   wigilia = datetime(dzisiaj.year, month, day)
#   if dzisiaj > wigilia:
#     wigilia = datetime(dzisiaj.year, month, day)
#   pozostalo = wigilia - dzisiaj
#   return pozostalo.days  #bez tego days z godzinami daje


# print(f"Do wigilii zostało {dni_do_Wigilii()} dni")

#zad 6
#Losuj prezent - napisz program, który wylosuje dwa rodzaje prezentów z dostępnej puli. Przykładowa pula: kosmetyki,  ubrania,  gry  książki, elektronikę,  inne. Możesz trzy razy losować, jeśli nie jesteś zadowolony z wyboru
# import random


# def losujprezent():
#   licznik = 0
#   limit = 3
#   running = True
#   while licznik < limit and running:
#     pula = ["kosmetyki", "ubrania", "gry", "książki", "elektronikę", "inne."]
#     p1 = random.choices(pula)
#     p2 = random.choices(pula)
#     print(f"{p1} {p2}")
#     licznik += 1
#     kontynuacja = input("Czy wybór Ci się podoba - tak/ nie? ").lower()
#     if kontynuacja == "tak":
#       running = False
#   else:
#     print("kto wybrzydza ten nic nie dostaje")

























#zad 7
#kalkulator zakupów - najpierw podaj ile chcesz kupić produktów, a potem pytaj się o kolejną cenę produktu, na końcu podaj kwotę zakupów, kwoty można podawać po przecinku
#wersja 2 bez limitu liczby produktów - pytaj się za każdym razem czy coś jeszcze, na końcu podaj wynik


def zakupy():
  max = int(input("ilosc "))
  licznik = 0
  kwota = 0
  while licznik < max:
    kwota += float(input("kwota "))
    licznik += 1
  else:
    print(f"\cena zakupów {kwota}")
print(zakupy())





























# def kalkulator_zakupow2():
#   kwota = 0
#   running = True
#   while running:
#     kwota += float(input("Podaj kwotę produktu "))
#     continuation = input("Coś jeszcze do zakupów tak/nie? ").lower()

#     if continuation != "tak":
#       running = False
#   else:
#     print(f"\nza zakupu zapłacisz {kwota}")


# kalkulator_zakupow2()

#zad 8 policz ile jest samogłosek w podanych przez użytkownika życzeniach świątecznych np. dla Wesołych Świąt podaje 5

# def liczsamogloski(str1):
#   samogloski="aeiouAEIUOąęóĄĘÓyY"
#   suma = 0
#   for i in str1:
#     if i in samogloski:
#       suma +=1
#   return suma

# print(liczsamogloski("Wesołych Świąt"))

# def najdluzszeslowo(str1):
#   slowa  = str1.split(" ")
#   maxi = len(slowa[0])
#   poz = 0
#   for i in range(len(slowa)):
#     if maxi < len(slowa[i]):
#       maxi = len(slowa[i])
#       poz = i
#   return slowa[poz]

# print(najdluzszeslowo("to jest moje megadługi ezdanie"))

# christmas_carol = '''
# Silent night! Holy night!
# All is calm, all is bright
# Round yon virgin mother and child!
# Holy infant, so tender and mild,
# Sleep in heavenly peace!
# Sleep in heavenly peace!
# '''
# liczba_slow = len(christmas_carol.split())
# # print(liczba_slow)



































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



