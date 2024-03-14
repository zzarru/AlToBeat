# BOJ 20164 G5 홀수 홀릭 호석

"""
입력받은 숫자의 길이가 1이면 홀수 갯수를 구해서 더해주고 return
길이가 2일 경우 반으로 쪼개서 다음 재귀로 넘어가면 됨
일이가 3이상이면 브루투포스를 통해 모든 경우를 다 재귀로 넘기면 됨
각 경우마다 최소와 최대를 비교해서
가장 큰 결과값과 작은 결과값을 저장
"""

N = input()


def count_odd_numbers(number):
    count = 0
    for n in number:
        if int(n) % 2:
            count += 1

    return count


def divide(n, count):
    global min_answer, max_answer
    count += count_odd_numbers(n)

    if len(n) == 1:
        min_answer = min(min_answer, count)
        max_answer = max(max_answer, count)
        return
    if len(n) == 2:
        divide(str(int(n) // 10 + int(n) % 10), count)
    else:
        for i in range(1, len(n) - 1):
            for j in range(i + 1, len(n)):
                temp = int(n[:i]) + int(n[i:j]) + int(n[j:])
                divide(str(temp), count)


min_answer, max_answer = 999999, 0
divide(N, 0)
print(min_answer, max_answer)
