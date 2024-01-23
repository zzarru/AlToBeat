nums = list(map(int, input().split()))

# 기준되는 idx를 정하고 뒤에 있는 숫자와 비교하며 정렬한다.
for idx in range(2):
    if idx == 0:
        for next in range(1, 3):
            if nums[idx] > nums[next]:
                nums[idx], nums[next] = nums[next], nums[idx]
    if idx == 1:
        if nums[idx] > nums[2]:
            nums[2], nums[idx] = nums[idx], nums[2]

print(*nums)
