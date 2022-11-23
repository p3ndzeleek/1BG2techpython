# a, g =int(input()), int(input())
# if (a+g)/2 > (a*g)**2:
#     print("Tak")
# else:
#     print("Nie")
# for i in range(100, 1000):
#     if i%10 == 100 ** (1/2):

w = int(input())
l = float(input())
for i in range(int(l*12)):
    w += w *0.005
print(w)

