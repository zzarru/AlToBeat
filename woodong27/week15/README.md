# Week15(투 포인터, Two Pointer)

리스트(배열)의 원소에 순차적으로 접근해야 할 때, 시작과 끝 점의 위치를 기록하면서 처리하는 알고리즘이다.

e.g : 길이가 2인 연속하는 부분수열들의 합을 구하고 싶다.

```python
numbers = [1, 2, 3, 4, 5]

end = 0
sum_value = 0
for start in range(len(numbers) - 2 + 1):
    # start(시작점)가 0 부터 3까지 증가한다.
    while end <= len(numbers):  # 시작점이 numbers의 길이보다 커지면 종료
        if end - start > 1:
            # e.g : start = 0, end = 1이면 길이가 2인 부분수열 하나가 완성 된다.
            # end와 start의 차이가 2 이상이면 부분수열의 길이가 2보다 큰 경우라서 탈출
            print(sum_value)
            sum_value -= numbers[start]
            break
        sum_value += numbers[end]
        end += 1

# 결과 : 3, 5, 7, 9
```

전반적으로 슬라이딩 윈도우와 비슷한 느낌의 알고리즘인 것 같다.
