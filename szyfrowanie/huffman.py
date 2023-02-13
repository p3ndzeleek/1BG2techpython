W = "MMMMMAAARRRRECCZZZEKK"
W += "."
#5m3a4r1e2c3z1e2k
# print(W[12])
# print(len(W))
ilośc = 1
H = ""
for i in range(len(W)-1):
    if W[i] == W[i+1]:
        ilośc += 1
    else:
        if ilośc > 1:
            H += str(ilośc) 
        H += W[i]
        ilośc = 1
print(H)