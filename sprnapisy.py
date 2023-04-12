
#gr2
# #zad1
# a = input()
# b = input()
# if a in b:
#     print("tak")
# else:
#     print("nie")
#zad2

# s = input()
# if s.count("a") >= 2 and s.count("b") >= 1 and s.count("z")>=1:
#     print("tak")
# else:
#     print("nie")



#zad3

s = input()
k = s
for i in range(len(s)):
    if s.count(s[i])>1:
        s.pop(s.index(s[i]))
#gr1
#zad3 
# s = input()
# for i in range(len(s)-1):
#     if s[i+1] < s[i]:
#         print("nie jest ok")
#         exit(0)
# print("jest ok")

