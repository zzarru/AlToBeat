import sys
input = sys.stdin.readline

T = int(input())
cnt = 0
for _ in range(T):
    letters = input()
    letters = letters.strip()
    box = []
    for letter in letters:
        if box: # 박스가 비어있지 않고
            if box[-1] == letter:
                box.pop()
            else:
                box.append(letter)
        else:  # 박스가 비어있다면
            box.append(letter)

    if len(box) == 0:
        cnt += 1
print(cnt)