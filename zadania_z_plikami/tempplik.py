# with open("temp.txt", "r") as file:
temperatura = file.read().split()

#zad 1
# ponizej_0 = sum(1 for temp in temperatures if int(temp) < 0)
# print(ponizej_0)

#zad 2
# min_temp = float(temperatures[0])
# for temp in temperatures:
#     if float(temp) < min_temp:
#         min_temp = float(temp)
# print(min_temp)

#zad 3
# srednia = sum(float(temp) for temp in temperatura) / len(temperatura)
# print(round(srednia, 2))

# #zad 4
# dodatnie_calkowite = sum(1 for temp in temperatura if float(temp).is_integer() and float(temp) > 0)
# print(dodatnie_calkowite)

# #zad 5
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

liczby_pierwsze = [int(temp) for temp in temperatura if is_prime(int(temp))]
print(liczby_pierwsze)
print(len(liczby_pierwsze))















# #zad 6
# kwadratowe = [int(temp) for temp in temperatura if int(temp) ** 0.5 == int(temp ** 0.5)]
# print(kwadratowe)
# print(len(kwadratowe))

# #zad 7
# szescienne = [int(temp) for temp in temperatura if int(temp) ** (1/3) == int(temp ** (1/3))]
# print(szescienne)
# print(len(szescienne))