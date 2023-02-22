#zad1
# w = "4G3E2T6W3H"
# w += "."
# ilosc = 1
# h = ""
# for i in range(len(w)-1):
#     if w[i] == w[i+1]:
#         ilosc += 1
#     else: 
#         if ilosc > 1:
#             h += str(ilosc)
#         h += w[i]
#         ilosc = 1
# print(h)

#zad2

# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# from math import gcd
# x,y = b,d
# iloczyn = x*y
# nwd = gcd(x,y)
# nww = iloczyn//nwd
# e = (nww//b)*a
# f = (nww//d)*c
# g = e+f
# print(f"{g}/{nww}")


a,b,c,d = int(input()),int(input()),int(input()),int(input())
from math import gcd
x,y = b,d
iloczyn = x*y
nwd = gcd(x,y)
nww = iloczyn//nwd
e = (nww//b)*a
f = (nww//d)*c
g = e+f
print(f"{g}/{nww}")

