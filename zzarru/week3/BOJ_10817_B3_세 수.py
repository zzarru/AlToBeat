#1 리스트와 정렬 메서드 사용하기
nums = list(map(int, input().split()))
# nums.sort()
# print(nums[1])

#2 메서드 사용하지 않고 직접 정렬 구현하기
for i in range(2):
    default = i
    for j in range(1, 3):
        if nums[default] > nums[j]:
            nums[default], nums[j] = nums[j], nums[default]

print(nums[1])

