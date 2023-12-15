# Zadanie 1
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej.
# Podaj dwa największe dzielniki otrzymanej liczby. Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr.

# liczba = 47
# lustrzana =  (liczba % 10)*10 + liczba//10
# suma = liczba + lustrzana
# print(f"{lustrzana}, {liczba}, {suma}")

# i = suma
# licznik = 0
# while i > 0 and licznik <2:
#   if suma % i == 0:
#     print(i, end=" ")
#     licznik += 1
#   i -= 1


# Zadanie 2
# Oblicz sumę dowolnej liczby dwucyfrowej i liczby lustrzanej. 
#Liczbę lustrzaną otrzymujemy z danej liczby przez przestawienie jej cyfr. 
#sprawdz czy dla kliku wybranych liczb otrzymana suma dzieli się przez sumę cyfr jednej z liczb dwucyfrowej - tj. czy np. 42 +24 dzieli się przez 6



# def czypodziel(liczba):
#   lustrzana = (liczba%10)*10 + liczba//10
#   dzielnik = liczba % 10 + liczba // 10
#   suma = liczba + lustrzana
#   return suma%dzielnaik==0

# print(czypodziel(76))
# print(czypodziel(36))


#Zadanie 5 
# Czy z podanych trzech boków można utworzyć trójkąt?
# def czy_trojkat(a,b,c):
#   return a+b>c and a+b>c and b+c>a

# print(czy_trojkat())


#zadanie 4
#Dwucyfrowa liczba została podzielona przez sumę swoich cyfr. oblicz resztę tego działania? Sprawdź dla kilku przypadków
# def najwieksza_reszta(liczba):
#   suma = (liczba % 10 ) * 10 + liczba // 10
#   return liczba%suma

# print(najwieksza_reszta(69))

