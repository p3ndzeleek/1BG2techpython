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

n = int(input())
a = 1
suma = 0
for i in range(1,n+1):
    b = i*i
    suma += a/b
    a += 2  
print(suma)

#ciąg wymagający 
#n = int(input())
# a = 2
# suma = 0
# for i in range(1, n + 1):
#     b = i ** 3 + 2
#     suma += a/b
#     a += 2
# print(suma)


