# #zad1 
# for i in range(1,31):
#     print(f"{i} listopad 2022")

#zad2

# for i in range(1, 10, 2):
#     print(i**2, "no kwadraty ma sie rozumieć")

#zad3

# for i in range(1000, 10000):
#     if i %379 ==0:
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
#zad6

# k = int(input())
# a = 0
# for i in range(0,2 * k,2):
#     a += i
# print(a)


#zad7

# m = int(input())
# a=0
# for i in range(11, m+1, 2):
#   a+=i
# print(a)




#zad8

# w0 = int(input("podaj kwote wejściową: "))
# l = int(input("podaj okres inwestycji(w miesiącach): "))
# wk = 0
# suma = wk
# for i in range(0, l * 0,5):
#     suma = suma + wk
#     print(suma)

#zad9
# n = int(input())
# suma = 0
# for i in range(21, n+1 , 100):
#   suma += i 
# print(suma)


#zad10

# for i in range(1,1000):
#   if i%10==i ** (1/2):
#     print(i)
#   elif i%100== i ** (1/2):
#     print(i)


        
        
#zad69

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