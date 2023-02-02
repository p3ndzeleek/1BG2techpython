tekst = "twoja stara"



slowa =  1
litery = 0

slownik = {}

for x in t:

    if x == " ":slowa += 1
    if x != " ":
        litery += 1
         if x in slownik:
             slownik[x] += 1
         else:
             slownik[x] = 1
 return slowa, litery, slownik



# string = "ABC for the purpose of LetterCounting program"
# print(string)
# words = 1 
# letters = 0 
# hash_table = {}
# for char in string:
#     char = char.lower()
#     if char  == ' ':
#         words+=1
#     else:
#         letters+=1
#         if char in hash_table:
#             hash_table[char]+=1
#         else:
#             hash_table[char]=1
                
# print("Words:", words, "Letters:", letters, "Freq:", hash_table)