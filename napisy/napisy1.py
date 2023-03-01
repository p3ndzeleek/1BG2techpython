# #napis jest prawie lista 
# s = input()

# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(s[i])


# L = [5,7,2,4]
# print(L)
# L.sort()
# print(L)
# s = input()
# print(s)
# s.sort() #"błąd napis to nie normalna lista"
# print(s)

# przechodzenie : napis <-> lista(list() i  join())

# s = input()
# L = list(s)
# print(s,L)
# L.sort()
# print(s,L)
# s = "-".join(L) #to sprawia że lista jest nzowy napisem ta buzka z przodu usuwa znaki pomiędzy
# print(s,L)

#wyraz od końca jest taki sam jak od początku
# s = input()
# l = list(s)
# r = l.copy()
# r.reverse()
# print(l,r)
# if l == r:
#     print("tak")
# else:
#     print("nie")


#2
s = input()
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        exit("nie")
exit("tak")