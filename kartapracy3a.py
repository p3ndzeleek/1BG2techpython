# #zad1
# n = int(input())
# for i in range(n):
#     print("*-|", end=" ")

# n = int(input())
# print("*-|"*n)
#zad2

# n = int(input())
# for i in range(1, n+1):
#     print("*"*i, end=" ")
#     if i % 2 == 1:
#         print("||", end=" ")
#     else:
#          print("--", end=" ")   

n = int(input())
znak = "--"
for i in range(1, n+1):
    print("*"*i, end=" ")
    if znak == "--":
        znak = "||"
    else:
        znak="--"
        print(znak, end=" ")
