# #zad1 
# for i in range(1,31):
#     print(i, "dni")

#zad2

# for i in range(1, 10, 2):
#     print(i**2, "no kwadraty ma sie rozumieć")

#zad3

# for i in range(1138, 9855):
#     if i %379 ==0:
#         print(i)

#zad4

# for i in range(101, 1000):
#     if i %5 ==0 and i %6 ==0 and i %11 ==0:
#         print(i)

#zad5

# a = int(input("podaj ilośc liczb: "))
# Liczby = []
# for i in range(0, a):
#     temp = int(input(f"Podaj {i+1} liczbę: "))
#     Liczby.append(temp)
# print(f"Wynik to: {sum(Liczby)}")

#zad6








#zad8

# w0 = int(input("podaj kwote wejściową: "))
# l = int(input("podaj okres inwestycji: "))
# for i in range(w0, l):
#     if (l*0.5):
#         print()


        
        
        
#zad69

def dick_draw():

    # ayy lmao u nigga gay
    i_want_more_dicks = 'Y'

    # vvv this line below thinks you're all into dicks and you probably love them, which in short, makes you really gay.
    while i_want_more_dicks == 'Y':

        # initialize variables to be filled in with loops later.
        shaft = '' # dick body units
        head = '' # dickhead type/shape
        cumshot = '' # jizz length (could be piss for you, but whatever)

        # input dick stats.
        dick_length = int(input('enter dick length (must be a number, enter 0 for a chode): '))
        while dick_length < 0:
            dick_length = int(input("i can't draw a retracted cock, you shit cunt! "))
        dickhead = int(input('enter dickhead type\nreference: o O 0 D (type a number 1-4): '))
        while dickhead < 1 or dickhead > 4:
            dickhead = int(input('enter a valid dickhead type you fuckwit! '))
        cumshot_length = int(input('enter cumshot length (must be a number, enter 0 for no jizz): '))
        while cumshot_length < 0:
            cumshot_length = int(input("a dick can't cum inside itself, you fucking faggot! "))

        # phallic algorithms in work.
        for dickflesh in range(dick_length):
            shaft = '=' * dick_length
        if dickhead == 1:
            head = 'o'
        if dickhead == 2:
            head = 'O'
        if dickhead == 3:
            head = '0'
        if dickhead == 4:
            head = 'D'
        for jizz_range in range(cumshot_length):
            cumshot = '~' * cumshot_length

        # your carefully crafted phallus is about to be provided. congratu-fucking-lations. cock successfully made.
        print("here's your dick:\n8" + shaft + head + cumshot)

        # if u type in yes there4 u rly gay lmao
        i_want_more_dicks = input('do you wish to draw a dick again? enter "Y" for yes, anything else for no: ')
dick_draw()