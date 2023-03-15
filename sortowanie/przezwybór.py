# wygenerój  10 ranodmowycb\h liczb

from random import randint
n = 10
l = [randint(1,30)for i in range(n)]
print(l)

for i in range(n):
    mi = i
    for j in range(i+1, n):
        if l[j] < l[mi]:
            mi = j

        l[i], l[mi] = l[mi], l[i
print(l)