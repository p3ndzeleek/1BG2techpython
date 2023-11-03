# a, b = int(input()), int(input())
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

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial())

#zad2

        






# def suma_liczb(n):
#     suma = 0
#     while n > 0 % 10 == 0:
#         suma += n % 10
#         n = n // 10
#     return suma

# n = int(input())  
# print(suma_liczb(n))


# def silnia_rek(a):
#     if a == 1:
#         return a 
#     else:
#         return a *(silnia_rek(a-1))

# def silnia_ite(a):
#     wynik = 1
#     while a>=1:
#         wynik *= a
#         a -=1
#     return wynik









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


