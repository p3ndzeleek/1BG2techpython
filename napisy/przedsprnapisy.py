# #1
# s = input()
# l = list(s)
# a = len(s)-1
# print(s[0], s[a])

# #2
# b = input()
# for i in range(1, len(b)-1):
#     print(b[i], end=" ")
# print()

#2 sposub
# l = list(b)
# l.pop(0)
# l.pop(-1)
# b = "".join(l)
# print(b)

#3
# c = input()
# l = list(c)
# l.reverse()
# c = "".join(l)
# print(c[:4])


#4 średnia z liter 
# d = input()
# s = 0 
# for x in d:
#     s += ord(x)
# znak = s // len(d)
# print(chr(znak))


#5 oblicznie ilości danego znaku np.a i ilośc samogłosek 

# e = input()
# ilosc = 0
# for x in e:
#     if x == "A":
#         ilosc += 1
# print(ilosc)

# SAMO = ["A", "E","I","O","U","Y"]

# ilosc_samo = 0
# for x in e:
#     if x in SAMO:
#         ilosc_samo += 1
# ilosc_samo

#6 

# f = input()
# maksiu = 0
# for x in f:
#     if f.count(x) > maksiu:
#         maksiu = f.count(x)
#         literka = x
# print(literka, maksiu)

#8 
h = input()
ilosc = 0
for i in range(len(h)):
    if h[i:i+2] == "LA":
        ilosc += 1
if ilosc == 3:
    print("taK")
else:
    print("NIe")

