n = int(input())
letters = []
for _ in range(n):
    l = input()
    if l not in letters:
        letters.append(l)

letters.sort()

for number in range(1, 51):
    for letter in letters:
        if number == len(letter):
            print(letter)