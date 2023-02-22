# # #nwd
# # a = int(input())
# # b = int(input())
# # iloraz = a * b
# # while a != b:
# #     if a > b : a = a - b
# #     if b > a : b = b - a
# # print(iloraz // a)


a = int(input())
b = int(input())
iloczyn = a * b
while b > 0:
    a ,b = b , a %b
print(iloczyn / a)

