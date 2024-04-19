def palindrome(a):
    left = 0
    right = len(a)-1
    while left < right:

        if a[left] == a[right]: #같다면 현재 데칼코마니인거
            left += 1
            right -= 1

        else: #데칼코마니가 깨졌을때

            if left<=right -1 : #해당 왼쪽숫자를 지운채로 펠린드롭검사
                temp= a[:right] + a[right + 1:]
                if temp[:]==temp[::-1]:
                    return 1

            if left + 1 <= right : #해당 오른쪽 숫자를 지운채로 렐린드롭검사
                temp = a[:left]+ a[left + 1:]
                if temp[:]==temp[::-1]:
                    return 1

            return 2 #앞선 오른쪽 문자와 왼쪽문자를 지운 경우가 성립안되면 가망없음
    return 0
for _ in range(int(input())):
    print(palindrome(input()))