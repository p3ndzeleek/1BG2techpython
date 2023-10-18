#zad1
a = input()
count = 0
for x in a:
    if x.isalpha():
        count += 1
print("liczba liter", a ,"to", count)

#zad2
# slowo = input("Podaj słowo: ")
# x = ""

# for i in range(len(slowo)):
#     if i % 2 == 0:
#         x += slowo[i+1] if i+1 < len(slowo) else slowo[i]
#     else:
#         x += slowo[i-1]

# print("Słowo przekształcone: " + x)