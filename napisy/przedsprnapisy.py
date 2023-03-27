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
c = input()
l = list(c)
l.reverse()
c = "".join(l)
print(c[:4])


