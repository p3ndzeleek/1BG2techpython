# T = [500, 200, 100, 50, 20, 10, 5, 2, 1]
# x = int(input())
# for i in T:
#     ilosc = x// i
#     if ilosc > 0:
#         x = x - ilosc * i
#         print(f"{ilosc} razy {i}")


T = [500, 200, 100, 50, 20, 10, 5, 2, 1]
x = int(input())
W = []
for i in T:
    ilosc = x// i
    if ilosc > 0:
        x = x - ilosc * i
        for j in range(ilosc):
            W.append(i)
print(W)
            
