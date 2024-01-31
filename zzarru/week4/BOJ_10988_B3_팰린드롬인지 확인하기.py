letter = input()

ans = 1
for front_idx in range(len(letter)):
    back_idx = -(front_idx+1)

    if letter[front_idx] != letter[back_idx]:
        ans = 0
        break

print(ans)
