  # a = int(input())
# b = int(input())
# c = int(input())
# if b-a == c-b:
#     print("tak")

# if b/a == c/b:
#     print("tak")

# if a<b<c:
#     print("tak")
# if a>b>c:
#     print("nie")

# suma = 0
# for i in range(101,1000):
#  if i %8 ==0 and i %16 !=0:
#      suma += i
# print(suma)


# for i in range(11,100):
#     if i %7 ==0:
#         wielokrotnosc = 1
# ilosc = 0 
# for i in range(100,10000):
#     if i % wielokrotnosc ==0:
#         ilosc += 1
# print(ilosc)
    
# ilosc = 0
# for i in range(10, 100):
#     if 2 * (i % 10) <= i // 10:
#         ilosc += 1
# print(ilosc)   

# n = int(input())
# suma = 0 
# for i in range(1, n+1):
#     il = 1
#     for i in range(1,i+1):
#         il = il * i
#     suma += il
# print(suma)


# niebanalny 1                        
#     b = i*i
#     suma += a/b
#     a += 2
 #niebalalny 2
#n = int(input())
# a = 1
# suma = 0
# sumb = 0
#for i in range(1,n+1):
#     suma += a
#     a += 2
#     b = i * i
#     sumb += b
 #ciąg wymagający 
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2


# Zad 15
# n = int(input())
# a = 3
# b = 1
# il = 1
# for i in range(n):
#     il *= a/b
#     a += 1
#     b = b * 2 + 1
# print(il)
# Zad 16
# n = int(input())
# a1 = 1
# a2 = 2
# b = 1
# il = 1
# for i in range(1, n + 1):
#     il *= a1/b
#     a1, a2 = a2, a1 + a2
#     b *= 2
# print(il)

# n = int(input())
# a = 1
# suma = 0
# for i in range(1,n+1):
#     b = i*i
#     suma += a/b
#     a += 2  
# print(suma)

#ciąg wymagający 
#n = int(input())
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2
# print(suma)


# napis = "Brzeczeszczykiewicz"


# print(list(napis

# py_str = "Learn how to use split() in Python"
# print(py_str.split())




# print(", ".join(["a", "b", "c"]))

# print("hello world".replace("hello", "siema kurwo")) #replace zmienia pierwsze słowo krore podamy w nawiasie na drogie napisane po przeciku

#palindrom wyraz jest taki sam od prawej i lewej
# s = input()
# l = list(s)
# r = l.copy()
# r.reverse()
# print(l,r)
# if l == r:
#     print("tak")
# else:
#     print("nie")

#2 sposób
# s = input()
# for i in range(len(s)//2):
#     if s[i] != s[len(s)-1-i]:
#         exit("nie")
# exit("tak")

#anagram wyraz z krorego liter można zrobic inny
# a = input()
# b = input()
# X, Y = list(a), list(b)
# X.sort()
# Y.sort()
# a ="".join(X)
# b ="".join(Y)
# print(a,b)
# if a == b:
#     print("tak")
# else:
#     print("nie")

#8 boyer moore sprawdza czy La występuje tyle razy ile wpiszemy w "if ilosc == :"
# h = input()
# ilosc = 0
# for i in range(len(h)):
#     if h[i:i+2] == "LA":
#         ilosc += 1
# if ilosc == 2:
#     print("taK")
# else:
#     print("NIe")




#wydawanie reszty
# T = [500, 200, 100, 50, 20, 10, 5, 2, 1]
# x = int(input())
# W = []
# for i in T:
#     ilosc = x//i
#     if ilosc >0:
#         x = x - ilosc * i 
#         for j in range(ilosc):
#             W.append(i)
# print(W)



#Grupa 2

#zadanie 1

# slowo1 = input("Wprowadź pierwsze słowo: ")
# slowo2 = input("Wprowadź drugie słowo: ")

# if slowo1 in slowo2:
#     print(f"Słowo '{slowo1}' jest zawarte w słowie '{slowo2}'")
# elif slowo2 in slowo1:
#   print(f"Słowo '{slowo2}' jest zawarte w słowie '{slowo1}'")
# else:
#     print(f"Słowo '{slowo1}' nie jest zawarte w słowie '{slowo2}'")

# #zadanie 2

# litery = input("Wprowadź litery: ")
# zbior_liter = set(litery)

# if "b" in zbior_liter and "a" in zbior_liter and "z" in zbior_liter:
#     print("Można utworzyć słowo 'baza' ze wprowadzonych liter.")
# else:
#     print("Nie można utworzyć słowa 'baza' ze wprowadzonych liter.")

# #zadanie 3

# slowo = input("Wprowadź słowo: ")
# nowe_slowo = ""

# for litera in slowo:
#     if slowo.count(litera) == 1:
#         nowe_slowo += litera

# print(f"Słowo bez powtarzających się liter: {nowe_slowo}")

# #Grupa 1

# #zadanie 1
# import re

# slowo = input("Wprowadź słowo: ")
# match = re.search(r"(.)(.*)(\1)", slowo)
# znaki = match.group(2) if match else ""

# print(f"Znaki między parą takich samych znaków: {znaki}")

# #zadanie 2

# slowo = input("Wprowadź słowo: ")
# nowe_slowo = ""

# for i in range(len(slowo)-2, -1, -2):
#     para = slowo[i:i+2][::-1]
#     nowe_slowo += para

# print(nowe_slowo)

# #zadanie 3
# a = input()
# X = list(a)
# Y = list(a)
# Y.sort(key=lambda y: y.lower())
# if X == Y:
#     print("TAK")
# else:
#     print("NIE")



# a = int(input())
# b = int(input())
# c = int(input())

# if a+b > c and a+c > b and b+c > a:
#     print("Liczby spełniają nierówność trójkąta")
# else:
#     print("Liczby nie spełniają nierówności trójkąta")


# a = float(input())
# b = float(input())
# c = float(input())

# if a + b > c and a + c > b and b + c > a:
#     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("Trójkąt jest prostokątny.")
#     elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#         print("Trójkąt jest rozwartokątny.")
#     else:
#         print("Trójkąt jest ostrokątny.")
# else:
#     print("Z podanych boków nie można zbudować trójkąta.")

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Trójkąt jest prostokątny."
        elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
            return "Trójkąt jest rozwartokątny."
        else:
            return "Trójkąt jest ostrokątny."
    else:
        return "Z podanych boków nie można zbudować trójkąta."

# Example usage:
a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))
print(check_triangle(a, b, c))


a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Trójkąt jest prostokątny.")
    elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print("Trójkąt jest rozwartokątny.")
    else:
        print("Trójkąt jest ostrokątny.")
else:
    print("Z podanych boków nie można zbudować trójkąta.")