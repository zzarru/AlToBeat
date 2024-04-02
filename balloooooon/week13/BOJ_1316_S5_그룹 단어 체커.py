'''

일단 해당 단어에서 중복을 제외한 철자리스트를 하나 만들고
단어를 순회하며 연속성을 확인한다.
연속성의 확인은 임시로 temp에 전의 철자를 저장한다.

철자가 들어온다? 중복체크한 철자리스트에서 해당 철자를 제거하고
temp에 철자를 저장한다.
그리고 연속성을 따진다.
만일 이산가족된 철자를 만날경우 해당 순회를 break한다.

'''

N = int(input())
answer = 0
for _ in range(N):
    word = input()
    is_Group_Word = 1
    spell_list = list(word)
    intersection = list(set(list(word)))


    temp = spell_list[0]

    for spell in spell_list:
        if spell in intersection:
            intersection.remove(spell)
            temp = spell
        else:
            if spell == temp:
                pass
            else:
                is_Group_Word = 0
                break
    if is_Group_Word:
        answer += 1
print(answer)