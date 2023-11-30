from string import ascii_lowercase

chr = input()
alphabet = list(ascii_lowercase)

for i in alphabet:
    print(chr.find(i), end=" ")